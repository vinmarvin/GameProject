using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

//Energy Bar UI

public class EnergyBar : MonoBehaviour
{
	public Slider slider;
	public Gradient gradient;
	public Image fill;
    public Image energyIcon;
    public Sprite fullEnergySprite;
    public Sprite midEnergySprite;
    public Sprite lowEnergySprite;

	public void SetMaxEnergy(float energy)
	{
		slider.maxValue = energy;
		slider.value = energy;

		fill.color = gradient.Evaluate(1f);
        UpdateIcon(energy);
	}

    public void SetEnergy(float energy)
	{
		slider.value = energy;

		fill.color = gradient.Evaluate(slider.normalizedValue);
        UpdateIcon(energy);
	}

    private void UpdateIcon(float energy)
    {
        if (energyIcon == null) return;

        float percentage = (energy / slider.maxValue) * 100f;
        if (percentage >= 65f)
        {
            energyIcon.sprite = fullEnergySprite;
        }
        else if (percentage >= 35f)
        {
            energyIcon.sprite = midEnergySprite;
        }
        else
        {
            energyIcon.sprite = lowEnergySprite;
        }
    }
}
