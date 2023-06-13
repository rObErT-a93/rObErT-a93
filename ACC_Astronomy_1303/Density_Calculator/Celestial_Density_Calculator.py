import tkinter as tk
from tkinter import messagebox
import re

# Regular expression pattern to validate scientific notation
scientific_notation_pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')

def validate_scientific_notation(input_str):
    """
    Validate the input string to ensure it is in scientific notation.
    """
    return bool(scientific_notation_pattern.match(input_str))

def calculate_density():
    try:
        mass = float(mass_entry.get())
        volume = float(volume_entry.get())

        density = (mass * 1000) / volume # Convert mass from kg to g
        messagebox.showinfo("Result", f"The Density is {density} g/cm^3")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

def validate_input(event):
    """
    Validate the input in the Entry fields as the user types.
    """
    widget = event.widget
    value = widget.get()

    if not validate_scientific_notation(value):
        widget.config(foreground="red")
    else:
        widget.config(foreground="black")


root = tk.Tk()
root.title("Celestial Density Calculator")

# Label and Entry for mass
mass_label = tk.Label(root, text="Mass (kg):")
mass_label.pack()
mass_entry = tk.Entry(root)
mass_entry.pack()
mass_entry.bind("<KeyRelease>", validate_input) # Bind input validation to the Entry field

# Label and Entry for volume
volume_label = tk.Label(root, text="Volume (m^3):")
volume_label.pack()
volume_entry = tk.Entry(root)
volume_entry.pack()
volume_entry.bind("<KeyRelease>", validate_input) # Bind input validaiton to the Entry field

#Button to calculate density
calculate_button = tk.Button(root, text="Calculate Density", command=calculate_density)
calculate_button.pack()

root.mainloop() 