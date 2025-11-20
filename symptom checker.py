import tkinter as tk
from tkinter import messagebox

# knowledge base
conditions = {
    "Fever": ("Possible viral fever", "Drink warm water, rest, stay hydrated"),
    "Cough": ("Possible common cold", "Drink warm water, avoid cold items, inhale steam"),
    "Headache": ("Possible stress or dehydration", "Rest, drink water, avoid screens for a while"),
    "Vomiting": ("Possible food poisoning", "Drink ORS, rest, avoid solid food temporarily"),
    "Stomach Pain": ("Possible acidity or indigestion", "Eat light food, drink warm water"),
    "Stress": ("Possible study stress", "Take a 10-minute break, breathe deeply"),
    "Sore Throat": ("Possible throat infection", "Gargle with warm salt water"),
}

# create main window
root = tk.Tk()
root.title("AI Symptom Checker")
root.geometry("400x550")   # <-- FIXED
root.config(bg="#f0f0f0")

title = tk.Label(root, text="AI Symptom Checker",
                 font=("Arial", 20, "bold"),
                 bg="#f0f0f0")
title.pack(pady=15)

sub = tk.Label(root, text="Select the symptom you are experiencing",
               font=("Arial", 12), bg="#f0f0f0")
sub.pack()

# Store checkbox variables
checkbox_vars = {}

# Add checkboxes
for symptom in conditions.keys():
    var = tk.BooleanVar()
    checkbox_vars[symptom] = var
    cb = tk.Checkbutton(root, text=symptom,
                        font=("Arial", 12),
                        variable=var, bg="#f0f0f0")
    cb.pack(anchor="w", padx=50)

# function to show diagnosis
def diagnose():
    selected = [sym for sym, var in checkbox_vars.items() if var.get()]
    if not selected:
        messagebox.showwarning("No input", "Please select at least one symptom.")
        return

    result = "---- DIAGNOSIS REPORT ----\n\n"

    for sym in selected:
        cond, advise = conditions[sym]
        result += f"Symptom: {sym}\n"
        result += f"Possible Condition: {cond}\n"
        result += f"Advice: {advise}\n\n"

    messagebox.showinfo("Diagnosis Result", result)

# button
btn = tk.Button(root, text="Check Symptoms", font=("Arial", 14, "bold"),
                bg="#4CAF50", fg="#ffffff",
                width=20, command=diagnose)
btn.pack(pady=20)

root.mainloop()
