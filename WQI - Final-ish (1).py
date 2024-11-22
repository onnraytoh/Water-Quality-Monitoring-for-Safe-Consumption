import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from skfuzzy import control as ctrl
from skfuzzy import membership as mf

# Define the antecedents for water quality parameters
ph_level = ctrl.Antecedent(np.arange(0, 14.1, 0.1), 'pH Level')
turbidity = ctrl.Antecedent(np.arange(0, 10, 0.1), 'Turbidity')
coliform = ctrl.Antecedent(np.arange(0, 20, 1), 'Coliform Bacteria')

# Define the consequent for water quality index and alert level
wqi = ctrl.Consequent(np.arange(0, 241, 1), 'Water Quality Index')
alert_level = ctrl.Consequent(np.arange(1, 101, 1), 'Alert Level')

# Define membership functions for pH Level
ph_level['acidic'] = mf.trapmf(ph_level.universe, [0, 0, 5, 5.5])
ph_level['slightly acidic'] = mf.trimf(ph_level.universe, [5.25, 6, 6.75])
ph_level['neutral'] = mf.trimf(ph_level.universe, [6.5, 7, 7.5])
ph_level['slightly alkaline'] = mf.trimf(ph_level.universe, [7.25, 8, 8.75])
ph_level['alkaline'] = mf.trapmf(ph_level.universe, [8.5, 9, 14, 14])

# Define membership functions for Turbidity
turbidity['low'] = mf.trapmf(turbidity.universe, [0, 0, 1, 1])
turbidity['moderate'] = mf.trimf(turbidity.universe, [1, 3, 5])
turbidity['high'] = mf.trapmf(turbidity.universe, [5, 6, 10, 10])

# Define membership functions for Coliform Bacteria
coliform['absent'] = mf.trapmf(coliform.universe, [0, 0, 1, 1])
coliform['moderate'] = mf.trimf(coliform.universe, [1, 5, 10])
coliform['high'] = mf.trapmf(coliform.universe, [10, 10, 20, 20])

# Define membership functions for Water Quality Index (WQI)
wqi['excellent'] = mf.trimf(wqi.universe, [0, 10, 20])
wqi['good'] = mf.trimf(wqi.universe, [20, 40, 60])
wqi['acceptable'] = mf.trimf(wqi.universe, [60, 100, 140])
wqi['unsafe'] = mf.trimf(wqi.universe, [140, 190, 240])

# Define membership functions for Alert Level on a scale of 1 to 100
alert_level['no action required'] = mf.trimf(alert_level.universe, [1, 5, 15])
alert_level['monitor closely'] = mf.trimf(alert_level.universe, [10, 28, 45])
alert_level['immediate action needed'] = mf.trimf(alert_level.universe, [40, 55, 70])
alert_level['emergency action needed'] = mf.trimf(alert_level.universe,[65, 83, 100])

# Define unique fuzzy rules
rule1 = ctrl.Rule(ph_level['neutral'] & turbidity['low'] & coliform['absent'], (wqi['excellent'], alert_level['no action required']))
rule2 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['low'] & coliform['absent'], (wqi['good'], alert_level['no action required']))
rule3 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['low'] & coliform['absent'], (wqi['good'], alert_level['no action required']))
rule4 = ctrl.Rule(ph_level['acidic'] & turbidity['low'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))
rule5 = ctrl.Rule(ph_level['alkaline'] & turbidity['low'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))

rule6 = ctrl.Rule(ph_level['neutral'] & turbidity['moderate'] & coliform['absent'], (wqi['good'], alert_level['monitor closely']))
rule7 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['moderate'] & coliform['absent'], (wqi['acceptable'], alert_level['monitor closely']))
rule8 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['moderate'] & coliform['absent'], (wqi['acceptable'], alert_level['monitor closely']))
rule9 = ctrl.Rule(ph_level['acidic'] & turbidity['moderate'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))
rule10 = ctrl.Rule(ph_level['alkaline'] & turbidity['moderate'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))

rule11 = ctrl.Rule(ph_level['neutral'] & turbidity['high'] & coliform['absent'], (wqi['unsafe'], alert_level['immediate action needed']))
rule12 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['high'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))
rule13 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['high'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))
rule14 = ctrl.Rule(ph_level['acidic'] & turbidity['high'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))
rule15 = ctrl.Rule(ph_level['alkaline'] & turbidity['high'] & coliform['absent'], (wqi['unsafe'], alert_level['emergency action needed']))

#Coliform Moderate
rule16 = ctrl.Rule(ph_level['neutral'] & turbidity['low'] & coliform['moderate'], (wqi['acceptable'], alert_level['monitor closely']))
rule17 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['low'] & coliform['moderate'], (wqi['acceptable'], alert_level['immediate action needed']))
rule18 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['low'] & coliform['moderate'], (wqi['acceptable'], alert_level['immediate action needed']))
rule19 = ctrl.Rule(ph_level['acidic'] & turbidity['low'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))
rule20 = ctrl.Rule(ph_level['alkaline'] & turbidity['low'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))

rule21 = ctrl.Rule(ph_level['neutral'] & turbidity['moderate'] & coliform['moderate'], (wqi['acceptable'], alert_level['immediate action needed']))
rule22 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['moderate'] & coliform['moderate'], (wqi['acceptable'], alert_level['immediate action needed']))
rule23 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['moderate'] & coliform['moderate'], (wqi['acceptable'], alert_level['immediate action needed']))
rule24 = ctrl.Rule(ph_level['acidic'] & turbidity['moderate'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))
rule25 = ctrl.Rule(ph_level['alkaline'] & turbidity['moderate'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))

rule26 = ctrl.Rule(ph_level['neutral'] & turbidity['high'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))
rule27 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['high'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))
rule28 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['high'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))
rule29 = ctrl.Rule(ph_level['acidic'] & turbidity['high'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))
rule30 = ctrl.Rule(ph_level['alkaline'] & turbidity['high'] & coliform['moderate'], (wqi['unsafe'], alert_level['emergency action needed']))

#Coliform High
rule31 = ctrl.Rule(ph_level['neutral'] & turbidity['low'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule32 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['low'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule33 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['low'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule34 = ctrl.Rule(ph_level['acidic'] & turbidity['low'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule35 = ctrl.Rule(ph_level['alkaline'] & turbidity['low'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))

rule36 = ctrl.Rule(ph_level['neutral'] & turbidity['moderate'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule37 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['moderate'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule38 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['moderate'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule39 = ctrl.Rule(ph_level['acidic'] & turbidity['moderate'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule40 = ctrl.Rule(ph_level['alkaline'] & turbidity['moderate'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))

rule41 = ctrl.Rule(ph_level['neutral'] & turbidity['high'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule42 = ctrl.Rule(ph_level['slightly acidic'] & turbidity['high'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule43 = ctrl.Rule(ph_level['slightly alkaline'] & turbidity['high'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule44 = ctrl.Rule(ph_level['acidic'] & turbidity['high'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))
rule45 = ctrl.Rule(ph_level['alkaline'] & turbidity['high'] & coliform['high'], (wqi['unsafe'], alert_level['emergency action needed']))

rules = [
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
    rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
    rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45
]

# Construct the fuzzy control system
water_quality_ctrl = ctrl.ControlSystem(rules=rules)
water_quality_system = ctrl.ControlSystemSimulation(control_system=water_quality_ctrl)

# # Define the input values
# water_quality_sim.input['pH Level'] = 10
# water_quality_sim.input['Turbidity'] = 2
# water_quality_sim.input['Coliform Bacteria'] = 2
#
# # Compute the outputs
# water_quality_sim.compute()
#
# # # Print the output values
# print("Water Quality Index:", water_quality_sim.output['Water Quality Index'])
#
# # Visualize the results
# ph_level.view()
# turbidity.view()
# coliform.view()
# wqi.view(sim=water_quality_sim)
# plt.show()

# Function to compute water quality based on fuzzy inputs
def compute_quality():
    # Set input values from sliders
    water_quality_system.input['pH Level'] = pH_slider.get()
    water_quality_system.input['Turbidity'] = turbidity_slider.get()
    water_quality_system.input['Coliform Bacteria'] = coliform_slider.get()
    water_quality_system.compute()

    # Get and display WQI output
    wqi_value = water_quality_system.output['Water Quality Index']
    if wqi_value <= 20:
        wqi_label.config(bg='green', text=f"Excellent: Safe for drinking \n WQI: {math.floor(wqi_value)}")
    elif 20 < wqi_value <= 60:
        wqi_label.config(bg='lightgreen', text=f"Good: Generally safe for drinking \n WQI: {math.floor(wqi_value)}")
    elif 60 < wqi_value <= 140:
        wqi_label.config(bg='yellow', text=f"Acceptable: Treatment advised \n WQI: {math.floor(wqi_value)}")
    else:
        wqi_label.config(bg='orange red', text=f"Unsafe: Not for drinking \n WQI: {math.floor(wqi_value)}")

    #Get alert value output
    alert_value = water_quality_system.output['Alert Level']
    alert_value_rounded = math.floor(alert_value)

    # Determine the alert level text based on the alert value
    if alert_value_rounded < 10:
        alert_text = "No Action Required"
        alert_color = 'green'
    elif 10 <= alert_value_rounded < 40:
        alert_text = "Monitor Closely - Be cautious"
        alert_color = 'yellow'
    elif 40 <= alert_value_rounded < 65:
        alert_text = "Immediate Action Required!"
        alert_color = 'orange'
    else:
        alert_text = "Emergency Action Needed - Critical situation"
        alert_color = 'red'

    # Update the alert label with the new text and color
    alert_label.config(text=f"{alert_text}\nAlert Level: {alert_value_rounded}", bg=alert_color)

# Plotting function for membership functions
def plot_memberships():
    fig, axes = plt.subplots(nrows=4, figsize=(6, 8))

    # Plot each membership function
    ph_level.view(ax=axes[0])
    axes[0].set_title('pH Level')

    turbidity.view(ax=axes[1])
    axes[1].set_title('Turbidity (NTU)')

    coliform.view(ax=axes[2])
    axes[2].set_title('Coliform Bacteria (CFU/100 mL)')

    wqi.view(ax=axes[3])
    axes[3].set_title('Water Quality Index')

    alert_level.view(ax=axes[3])
    axes[3].set_title('Alert Level')

    plt.tight_layout()
    return fig

# Update progress bar and label value when slider changes
def update_module(value, progress, label, param_name):
    value = float(value)
    progress['value'] = value
    label.config(text=f"{param_name}: {value:.1f}")

# Initialize the main window
root = tk.Tk()
root.title("Fuzzy Water Quality Assessment System")
root.geometry("800x450")
s = ttk.Style()
s.theme_use('classic')

# Frame for all parameter modules
main_frame = tk.Frame(root)
main_frame.pack(pady=20, padx=20, expand=True, fill="both")

# Frame for the parameter modules
modules_frame = tk.Frame(main_frame)
modules_frame.pack(pady=10)

# Parameter modules
modules = {}
for i, (param_name, param_min, param_max, resolution) in enumerate([
    ("pH Level", 0, 14, 0.1),
    ("Turbidity (NTU)", 0, 10, 0.1),
    ("Coliform (CFU/100 mL)", 0, 20, 1)
]):
    # Create a frame for each parameter with fixed size
    frame = tk.Frame(modules_frame, bd=2, relief="groove", padx=10, pady=10, width=180, height=3000)
    frame.grid(row=0, column=i, padx=12, pady=12, sticky="n")

    # Progress bar
    progress = ttk.Progressbar(frame, orient="horizontal", length=150, mode="determinate", maximum=param_max)
    progress.pack(pady=5)

    # Value label
    value_label = tk.Label(frame, text=f"{param_name}: {param_min}", font=("Arial", 12))
    value_label.pack()

    # Slider
    slider = tk.Scale(frame, from_=param_min, to=param_max, orient="horizontal", resolution=resolution,
                      command=lambda v, p=progress, l=value_label, name=param_name: update_module(v, p, l, name))
    slider.pack(pady=5)

    # Store slider references for later
    modules[param_name] = {'slider': slider, 'progress': progress}

# Aliasing sliders to match with compute_quality function
pH_slider = modules["pH Level"]["slider"]
turbidity_slider = modules["Turbidity (NTU)"]["slider"]
coliform_slider = modules["Coliform (CFU/100 mL)"]["slider"]

# Output label for Water Quality Index
wqi_label = tk.Label(root, text="WQI: --", font=("Arial", 14), width=40, height=2, relief="sunken")
wqi_label.pack(pady=10)

# Output label for Alert Level
alert_label = tk.Label(root, text="Alert Level: --", font=("Arial", 14), width=40, height=2, relief="sunken")
alert_label.pack(pady=10)

# Simulate Button
simulate_btn = ttk.Button(root, text="Simulate", command=compute_quality, style="TButton")
simulate_btn.pack(pady=20, ipadx=40, ipady=10)
# Configure a custom style for the button with a larger font
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 15, "bold"))

# Plot and display the membership functions
#fig = plot_memberships()

root.mainloop()