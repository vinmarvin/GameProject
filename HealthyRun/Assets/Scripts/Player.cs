using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Player : MonoBehaviour
{
    [Header("Movement Settings")]
    public float baseSpeed = 10f;
    public float playerJumpForce = 8f;

    [Header("Lane Settings")]
    public float laneDistance = 19f;
    public float laneChangeSpeed = 20f;
    private int currentLane = 0; // 0 = center, -1 = left, 1 = right

    [Header("Energy Settings")]
    public float maxEnergy = 100f;
    public float currentEnergy;
    public float energyDepletionRate = 2f; 
    public EnergyBar energyBar;
    
    [Header("Fast Food Boost Settings")]
    public int fastFoodThreshold = 5;
    public float speedBoostAmount = 3f;
    public float speedBoostDuration = 5f;
    private int fastFoodCount = 0;
    private bool isSpeedBoosted = false;
    
    private bool isGameOver = false;

    void Start()
    {
        currentEnergy = maxEnergy;
        if (energyBar != null)
        {
            energyBar.SetMaxEnergy(maxEnergy);
        }
    }

    void Update()
    {
        if (isGameOver) return;
        HandleMovement();
        HandleEnergyDepletion();
        UpdateEnergyUI();
    }

    private void HandleMovement()
    {
        jump();
        // Menggunakan GetCurrentSpeed() alih-alih baseSpeed langsung
        transform.Translate(Vector3.forward * Time.deltaTime * GetCurrentSpeed());
        
        if (Input.GetKeyDown(KeyCode.A) || Input.GetKeyDown(KeyCode.LeftArrow))
        {
            currentLane--;
            if (currentLane < -1) currentLane = -1; // Limit to left lane
        }
        else if (Input.GetKeyDown(KeyCode.D) || Input.GetKeyDown(KeyCode.RightArrow))
        {
            currentLane++;
            if (currentLane > 1) currentLane = 1; // Limit to right lane
        }

        Vector3 targetPosition = transform.position;
        targetPosition.x = currentLane * laneDistance;

        transform.position = Vector3.MoveTowards(transform.position, targetPosition, laneChangeSpeed * Time.deltaTime);
    }

    public float GetCurrentSpeed()
    {
    //Dynamic Speed Logic (Addition/Reduce Speed based on distance or energy)
    float distanceBoost = Mathf.Floor(transform.position.z / 600f) * 1f;
    float energyPercentage = (currentEnergy / maxEnergy) * 100f; //Change energy to percentage, to make accurate condition
    float speed = baseSpeed + distanceBoost;

    
    // Speed penalty based on energy
    if (energyPercentage < 30f)
    {
        speed -= 4f;
    }
    else if (energyPercentage < 65f)
    {
        speed -= 2f;
    }
    
    // Minimum speed clamp
    return Mathf.Max(speed, 2f);
}

    private void jump()
    {
        if (Input.GetKeyDown(KeyCode.W) || Input.GetKeyDown(KeyCode.UpArrow))
        {
            GetComponent<Rigidbody>().AddForce(Vector3.up * playerJumpForce, ForceMode.Impulse);
        }
    }

    private void HandleEnergyDepletion()
    {
        currentEnergy -= energyDepletionRate * Time.deltaTime;

        if (currentEnergy <= 0)
        {
            GameOver();
        }
    }

    public void AddEnergy(float amount)
    {
        currentEnergy += amount;
        if (currentEnergy > maxEnergy)
        {
            currentEnergy = maxEnergy;
        }
    }

    public void TakeHazardDamage(float damageAmount)
    {
        currentEnergy -= damageAmount;
    }

    public void AddFastFoodCombo()
    {
        fastFoodCount++;
        if (fastFoodCount >= fastFoodThreshold && !isSpeedBoosted)
        {
            StartCoroutine(SpeedBoostCoroutine());
        }
    }

    private IEnumerator SpeedBoostCoroutine()
    {
        isSpeedBoosted = true;
        fastFoodCount = 0; // Reset hitungan

        baseSpeed += speedBoostAmount;
        Debug.Log("Junk Food Combo! Kecepatan bertambah menjadi: " + baseSpeed);

        yield return new WaitForSeconds(speedBoostDuration);

        // Pastikan tidak error jika game sudah over sebelum efek habis
        if (!isGameOver) 
        {
            baseSpeed -= speedBoostAmount;
            isSpeedBoosted = false;
            Debug.Log("Efek Junk Food Habis! Kecepatan kembali menjadi: " + baseSpeed);
        }
    }

    private void UpdateEnergyUI()
    {
        if (energyBar != null)
        {
            energyBar.SetEnergy(currentEnergy);
        }
    }

    private void GameOver()
    {
        isGameOver = true;
        currentEnergy = 0;
        baseSpeed = 0;
        Debug.Log("Game Over! Kehabisan Energi.");
        UpdateEnergyUI(); 

        if (GameManager.Instance != null)
        {
            GameManager.Instance.TriggerGameOver();
        }
    }
}