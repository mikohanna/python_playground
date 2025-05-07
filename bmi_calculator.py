# BMI Calculator
# Calculates the Body Mass Index (BMI) for height (in meters) and weight (in kilograms).
def calc_bmi(height, weight):
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers.")
    
    bmi = weight / (height ** 2)
    bmi_result = ""
    conclusion = ""
    if bmi < 18.5:
        bmi_result = "Underweight"
        conclusion = f"You need to gain at least {round(18.5 * (height ** 2) - weight, 2)} kg to reach a normal weight."
    elif 18.5 <= bmi < 24.9:
        bmi_result = "Normal weight"
        conclusion = f"You are at a healthy weight. Congratulations!"
    elif 25 <= bmi < 29.9:
        bmi_result = "Overweight"
        conclusion = f"You need to lose at least {round(weight - 24.9 * (height ** 2), 2)} kg to reach a normal weight."
    elif 30 <= bmi < 34.9: 
        bmi_result = "Obesity (Class 1)"
        conclusion = f"You need to lose at least {round(weight - 24.9 * (height ** 2), 2)} kg to reach a normal weight."
    elif 35 <= bmi < 39.9:
        bmi_result = "Obesity (Class 2)"
        conclusion = f"You need to lose at least {round(weight - 24.9 * (height ** 2), 2)} kg to reach a normal weight."
    elif bmi >= 40:
        bmi_result = "Obesity (Class 3)"
        conclusion = f"You need to lose at least {round(weight - 24.9 * (height ** 2), 2)} kg to reach a normal weight."
    return f"Your BMI index is {round(bmi, 2)}. You are classified as: {bmi_result}. {conclusion}"

print(calc_bmi(1.85, 60))  # Example usage: height = 1.75m, weight = 70kg