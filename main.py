import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Variables for buttons
unit = tk.StringVar(value="metric")  # stores selected unit
show = tk.BooleanVar()               # stores checkbox state
