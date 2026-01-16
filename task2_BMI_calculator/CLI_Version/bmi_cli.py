def calculate_bmi():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        print(f"Category: {category}")
        
    except ValueError:
        print("Please enter valid numbers.")

calculate_bmi()
