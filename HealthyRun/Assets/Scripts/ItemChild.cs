using UnityEngine;

public class ItemChild : MonoBehaviour
{
    private CollectedItem parentGroup;

    void Start()
    {
        //Get component from parent object
        parentGroup = GetComponentInParent<CollectedItem>();

        if (parentGroup == null)
        {
            Debug.LogWarning("ItemChild tidak menemukan script CollectedItem di Parent-nya! Pastikan object ini ada di dalam grup yang benar.", gameObject);
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player") && parentGroup != null)
        {
            Player playerScript = other.GetComponent<Player>();

            if (playerScript != null)
            {
                // Type of Item
                if (parentGroup.itemType == CollectedItem.ItemType.Veggie)
                {
                    playerScript.AddEnergy(parentGroup.effectAmount);
                    Debug.Log("Veggie Collected dari Grup! Energy ditambahkan: " + parentGroup.effectAmount);
                }
                else if (parentGroup.itemType == CollectedItem.ItemType.FastFood)
                {
                    playerScript.TakeHazardDamage(parentGroup.effectAmount);
                    Debug.Log("Fast Food Collected dari Grup! Energy berkurang: " + parentGroup.effectAmount);
                }
            }

            GameObject targetToDestroy = parentGroup.gameObject;

            if (targetToDestroy.name.Contains("Veggies") || targetToDestroy.name.Contains("Junk") || targetToDestroy.name.Contains("Items"))
            {
                Transform itemRoot = transform;
                while (itemRoot.parent != null && itemRoot.parent.gameObject != targetToDestroy)
                {
                    itemRoot = itemRoot.parent;
                }
                targetToDestroy = itemRoot.gameObject;
            }

            Destroy(targetToDestroy);
        }
    }
}
