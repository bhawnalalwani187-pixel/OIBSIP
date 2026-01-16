import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
from datetime import datetime

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive.")
            return
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        label_result.config(text=f"BMI: {bmi:.2f} ({category})")
        
        # Save data
        with open("bmi_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), weight, height, round(bmi,2), category])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def show_trends():
    dates, bmis = [], []
    try:
        with open("bmi_data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                dates.append(row[0])
                bmis.append(float(row[3]))
        plt.plot(dates, bmis, marker='o')
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.title("BMI Trend Over Time")
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        messagebox.showerror("Error", "No data found.")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

tk.Label(root, text="Height (m):").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2)
label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Show BMI Trends", command=show_trends).grid(row=4, column=0, columnspan=2)

root.mainloop()
