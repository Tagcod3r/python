import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert cm to meters
    bmi = weight / (height ** 2)
    result_label.config(text=f"BMI: {bmi:.2f}")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (cm):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate", command=calculate_bmi).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
