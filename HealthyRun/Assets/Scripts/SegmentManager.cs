using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class EnvironmentZone
{
    public string zoneName;
    [Tooltip("Batas jarak maksimal Z (dalam meter) di mana zona ini berakhir")]
    public float endDistance; 
    public GameObject[] zonePrefabs;
    
    [Header("Items & Obstacles")]
    [Tooltip("Daftar item/obstacle yang khusus muncul di zona ini")]
    public GameObject[] zoneItems;
    [Tooltip("Peluang munculnya item di setiap blok jalan zona ini (0 = tidak pernah, 1 = selalu)")]
    [Range(0f, 1f)] public float itemSpawnChance = 0.8f;
}

public class SegmentManager : MonoBehaviour
{
    [Header("Environment Zones")]
    public EnvironmentZone[] environmentZones;

    [Header("Item Spawning")]
    [Tooltip("Hubungkan script ItemSpawner ke sini")]
    public ItemSpawner itemSpawner;

    [Header("Segment Settings")]
    [Tooltip("Panjang dari setiap segmen. Sesuaikan dengan ukuran segmen Anda (misal 200)")]
    public float segmentLength = 200f;
    [Tooltip("Centang ini jika titik pivot (sumbu) prefab Anda berada di tengah-tengah segmen, bukan di ujung awal.")]
    public bool isPivotInCenter = true; // Ditambahkan untuk memperbaiki isu segmen telat hancur
    [Tooltip("Jumlah segmen yang langsung di-spawn saat game baru dimulai")]
    public int initialSegments = 6; 
    [Tooltip("Segmen pertama yang sudah diletakkan manual di layar (agar tidak kosong saat Edit Mode)")]
    public GameObject startingSegment;
    
    [Header("Player Tracking")]
    public Transform playerTransform;
    [Tooltip("Jarak di depan player (Z) untuk memicu spawn segmen baru")]
    public float distanceToSpawn = 800f; 
    [Tooltip("Jarak di belakang player (Z) setelah melewati segmen, untuk menghapus segmen tersebut agar tidak berat")]
    public float distanceToDestroy = 15f; 

    private float spawnZ = 0f;
    private List<GameObject> activeSegments = new List<GameObject>();

    void Start()
    {
        if (playerTransform == null)
        {
            Player player = FindObjectOfType<Player>();
            if (player != null) playerTransform = player.transform;
        }

        if (startingSegment != null)
        {
            activeSegments.Add(startingSegment);
            spawnZ = startingSegment.transform.position.z + segmentLength;
            initialSegments -= 1; 
        }

        for (int i = 0; i < initialSegments; i++)
        {
            SpawnSegment(); 
        }
    }

    void Update()
    {
        if (playerTransform == null) return;

        // Gunakan while, bukan if, agar script otomatis memanggil jalanan
        // sebanyak-banyaknya di 1 frame sampai jarak pandangnya (distanceToSpawn) tertutupi penuh.
        while (playerTransform.position.z + distanceToSpawn > spawnZ)
        {
            SpawnSegment();
        }

        if (activeSegments.Count > 0)
        {
            // Menghitung batas akhir segmen tertua berdasarkan posisi Pivot
            float oldestSegmentEndZ = activeSegments[0].transform.position.z;
            if (isPivotInCenter)
            {
                // Jika pivot di tengah, maka ujung akhir segmen adalah (posisi + setengah panjangnya)
                oldestSegmentEndZ += segmentLength / 2f;
            }
            else
            {
                // Jika pivot di ujung awal, maka ujung akhirnya adalah (posisi + panjang penuh)
                oldestSegmentEndZ += segmentLength;
            }
            
            if (playerTransform.position.z > oldestSegmentEndZ + distanceToDestroy)
            {
                DestroyOldestSegment();
            }
        }
    }

    private EnvironmentZone GetZoneForDistance(float distance)
    {
        if (environmentZones == null || environmentZones.Length == 0) return new EnvironmentZone();

        // Cari zona yang batas akhirnya masih lebih besar dari jarak saat ini
        foreach (var zone in environmentZones)
        {
            if (distance <= zone.endDistance)
            {
                return zone;
            }
        }
        // Jika sudah melebihi semua zona, gunakan zona paling akhir
        return environmentZones[environmentZones.Length - 1]; 
    }

    private void SpawnSegment()
    {
        EnvironmentZone currentZone = GetZoneForDistance(spawnZ);

        if (currentZone.zonePrefabs == null || currentZone.zonePrefabs.Length == 0)
        {
            Debug.LogError("ERROR: Tidak ada prefab di zona '" + currentZone.zoneName + "'! Tolong isi minimal 1 prefab di Inspector. Mencegah freeze dengan memajukan spawnZ...");
            spawnZ += segmentLength; // <-- INI SANGAT PENTING untuk mencegah infinite loop
            return;
        }

        // Pilih segmen secara acak dari array zona saat ini
        int randomIndex = Random.Range(0, currentZone.zonePrefabs.Length);
        GameObject segmentPrefab = currentZone.zonePrefabs[randomIndex];

        // Instantiate segmen baru di posisi Z saat ini (spawnZ)
        GameObject newSegment = Instantiate(segmentPrefab, new Vector3(0, 0, spawnZ), Quaternion.identity);
        
        // Simpan ke dalam list agar bisa dilacak
        activeSegments.Add(newSegment);

        // --- ITEM SPAWNER LOGIC ---
        if (itemSpawner != null)
        {
            // Tentukan awal dari batas fisik segmen untuk perhitungan spawn Z acak
            float segmentStartZ = spawnZ;
            if (isPivotInCenter)
            {
                segmentStartZ -= (segmentLength / 2f);
            }
            
            // Panggil ItemSpawner dan berikan info zona saat ini
            itemSpawner.SpawnItemsForSegment(newSegment, segmentStartZ, segmentLength, currentZone.zoneItems, currentZone.itemSpawnChance);
        }

        // Majukan spawnZ sejauh ukuran segmen untuk spawn berikutnya
        spawnZ += segmentLength;
    }

    private void DestroyOldestSegment()
    {
        // Ambil segmen dari urutan pertama (paling belakang secara posisi)
        GameObject oldSegment = activeSegments[0];
        
        // Hapus dari list
        activeSegments.RemoveAt(0);
        
        // Hancurkan objectnya dari game untuk menghemat memori
        Destroy(oldSegment);
    }
}
