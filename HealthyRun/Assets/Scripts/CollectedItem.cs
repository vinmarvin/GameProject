using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CollectedItem : MonoBehaviour
{
    public enum ItemType { Veggie, FastFood }
    
    [Header("Item Settings")]
    public ItemType itemType;
    public float effectAmount = 10f;
    
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            Player playerScript = other.GetComponent<Player>();
            
            if (playerScript != null)
            {
                if (itemType == ItemType.Veggie)
                {
                    playerScript.AddEnergy(effectAmount);
                    Debug.Log("Veggie Collected! Energy ditambahkan: " + effectAmount);
                }
                else if (itemType == ItemType.FastFood)
                {
                    playerScript.TakeHazardDamage(effectAmount);
                    playerScript.AddFastFoodCombo(); 
                    Debug.Log("Fast Food Collected! Energy berkurang: " + effectAmount);
                }
            }
            
            Destroy(gameObject);
        }
    }
}
