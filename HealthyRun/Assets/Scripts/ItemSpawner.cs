using UnityEngine;

public class ItemSpawner : MonoBehaviour
{
    [Header("Spawn Settings")]
    [Tooltip("Jarak X antar jalur. Pastikan sama dengan Player.laneDistance")]
    public float laneDistance = 19f; 
    [Tooltip("Maksimal item yang muncul di dalam 1 blok segmen jalan")]
    public int maxItemsPerSegment = 3;

    [Header("Vertical Settings")]
    [Tooltip("Peluang item melayang di udara (0.0 = selalu di tanah, 1.0 = selalu di udara)")]
    [Range(0f, 1f)]
    public float jumpItemChance = 0.3f;
    [Tooltip("Ketinggian item saat berada di tanah")]
    public float groundY = 1f;
    [Tooltip("Ketinggian item saat melayang di udara (butuh lompat)")]
    public float jumpY = 5f;

    /// <summary>
    /// Dipanggil oleh SegmentManager saat segmen baru terbuat
    /// </summary>
    public void SpawnItemsForSegment(GameObject segment, float startZ, float segmentLength, GameObject[] allowedItems, float spawnChance)
    {
        // Jangan spawn jika zona ini tidak punya item atau peluang gacha gagal
        if (allowedItems == null || allowedItems.Length == 0) return; 
        if (Random.value > spawnChance) return; 

        // Tentukan jumlah item yang akan di-spawn di jalan ini
        int itemsToSpawn = Random.Range(1, maxItemsPerSegment + 1);
        
        for (int i = 0; i < itemsToSpawn; i++)
        {
            // Tentukan jalur (Kiri: -1, Tengah: 0, Kanan: 1)
            int randomLane = Random.Range(-1, 2); 
            float spawnX = randomLane * laneDistance;

            // Tentukan posisi Z acak di dalam rentang segmen ini
            // Margin 5f agar item tidak persis berada di ujung garis batas antar segmen
            float spawnZ = startZ + Random.Range(5f, segmentLength - 5f);

            // Tentukan posisi Y (Ketinggian)
            float spawnY = groundY; 
            if (Random.value < jumpItemChance) 
            {
                spawnY = jumpY; // Memaksa player untuk melakukan Jump
            }

            // Tentukan item secara acak dari daftar yang diberikan oleh zona
            GameObject itemPrefab = allowedItems[Random.Range(0, allowedItems.Length)];

            // Spawn item
            Vector3 spawnPosition = new Vector3(spawnX, spawnY, spawnZ);
            GameObject spawnedItem = Instantiate(itemPrefab, spawnPosition, Quaternion.identity);

            // Jadikan item sebagai child dari segmen agar otomatis hancur saat segmen lewat dan terhapus
            spawnedItem.transform.SetParent(segment.transform);
        }
    }
}
