import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Variables for buttons
unit = tk.StringVar(value="metric")  # stores selected unit
show = tk.BooleanVar()               # stores checkbox state


# Function to calculate BMI
def calc():
    try:
        m = float(entry_mass.get())     # get mass input
        h = float(entry_height.get())   # get height input
    except:
        label_result.config(text="Enter numbers")  # error message
        return

    # Choose formula based on unit
    if unit.get() == "metric":
        bmi = m / (h**2)
    else:
        bmi = 703 * m / (h**2)
