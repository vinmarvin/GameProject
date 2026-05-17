using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance;

    [Header("UI Panels")]
    public GameObject gameOverPanel;
    public GameObject winPanel;

    [Header("Target Distance Settings")]
    public float targetDistance = 5000f; 
    private float currentDistanceLeft;
    
    [Tooltip("Isi dengan UI Text. Jika pakai TextMeshPro, ubah tipe data menjadi TMPro.TMP_Text")]
    public TextMeshProUGUI distanceText;

    private Player playerController;
    private bool isGameActive = false;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
        }
        else
        {
            Destroy(gameObject);
        }
    }

    void Start()
    {
        Time.timeScale = 1f;
        if (gameOverPanel != null)
        {
            gameOverPanel.SetActive(false);
        }
        if (winPanel != null)
        {
            winPanel.SetActive(false);
        }

        currentDistanceLeft = targetDistance;
        playerController = FindObjectOfType<Player>();
        isGameActive = true;

        UpdateDistanceUI();
    }

    void Update()
    {
        if (isGameActive && playerController != null)
        {
            //Distance Covered (Explored to finish line)
            float distanceCovered = playerController.GetCurrentSpeed() * Time.deltaTime;
            currentDistanceLeft -= distanceCovered;

            if (currentDistanceLeft <= 0)
            {
                currentDistanceLeft = 0;
                TargetReached();
            }

            UpdateDistanceUI();
        }
    }

    private void UpdateDistanceUI()
    {
        if (distanceText != null)
        {
            //Make a Clean UI
            distanceText.text = Mathf.CeilToInt(currentDistanceLeft).ToString() + " METER\nLEFT";
        }
    }

    public void TriggerGameOver()
    {
        Debug.Log("Game Over");
        isGameActive = false;

        if (gameOverPanel != null)
        {
            gameOverPanel.SetActive(true);
        }
        Time.timeScale = 0f;
    }

    public void TargetReached()
    {
        Debug.Log("Target Reached! Player wins!");
        isGameActive = false;

        if (winPanel != null)
        {
            winPanel.SetActive(true);
        }
        Time.timeScale = 0f;
    }

    public void RestartGame()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }
}
