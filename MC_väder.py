import numpy as np
# -*- coding: utf-8 -*-

# Parametrar för vädersimuleringen
avg_temp = 20               # Genomsnittlig temperatur för månaden i grader Celsius
temp_std_dev = 5            # Standardavvikelse i temperatur
num_days = 30               # Antal dagar framåt vi vill simulera
num_simulations = 1000      # Antal Monte Carlo-simuleringar

# Simulering av temperaturer
temp_paths = np.zeros((num_simulations, num_days))

for i in range(num_simulations):
    for t in range(num_days):
        # Slumpmässigt genererad temperatur baserat på normalfördelning
        temp_paths[i, t] = np.random.normal(avg_temp, temp_std_dev)

# Visa resultatet av simuleringen
plt.figure(figsize=(10, 5))
plt.plot(temp_paths.T, alpha=0.1)  # Visa varje simulering med låg opacitet
plt.title("Monte Carlo-simulering av temperaturer över 30 dagar")
plt.xlabel("Dag")
plt.ylabel("Temperatur (°C)")
plt.show()
