import tkinter as tk

def calculate_egfr():
    try:
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        serum_creatinine = float(creatinine_entry.get())
        is_male = male_var.get()

        if is_male:
            constant = 1
        else:
            constant = 0.85

        creatinine_clearance = ((140 - age) * weight) / (serum_creatinine * 72) * constant
        egfr = creatinine_clearance * 0.0113

        result_label.config(text="eGFR: {}".format(egfr))

    except ValueError as e:
        result_label.config(text="Error: {}".format(str(e)))

# Create the main window
window = tk.Tk()
window.title("eGFR Calculator")

# Create input labels and entry fields
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

creatinine_label = tk.Label(window, text="Serum Creatinine (mg/dL):")
creatinine_label.pack()
creatinine_entry = tk.Entry(window)
creatinine_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()

male_var = tk.BooleanVar()
male_radio = tk.Radiobutton(window, text="Male", variable=male_var, value=True)
male_radio.pack()

female_radio = tk.Radiobutton(window, text="Female", variable=male_var, value=False)
female_radio.pack()

# Create the Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_egfr)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
