# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Parametrar för aktiesimuleringen
initial_price = 100         # Startkurs för aktien
mu = 0.05                    # Förväntad avkastning (drift) i procent per tidsenhet
sigma = 0.2                  # Volatilitet (standardavvikelse av avkastning)
time_horizon = 1             # Tidsperiod (t.ex. ett år)
num_simulations = 1000       # Antal Monte Carlo-simuleringar
time_steps = 252             # Antal tidsteg (t.ex. antal börsdagar på ett år)

# Simulering av aktiekurs
dt = time_horizon / time_steps  # Tidssteg
price_paths = np.zeros((num_simulations, time_steps + 1))
price_paths[:, 0] = initial_price

for i in range(num_simulations):
    for t in range(1, time_steps + 1):
        # Slumpmässig förändring baserad på normalfördelning
        random_change = np.random.normal(0, 1)
        # Prisförändring enligt geometrisk Brownsk rörelse
        price_paths[i, t] = price_paths[i, t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * random_change)

# Visa resultatet av simuleringen
plt.figure(figsize=(10, 5))
plt.plot(price_paths.T, alpha=0.1)  # Visa varje simulering med låg opacitet
plt.title("Monte Carlo-simulering av aktiekurs")
plt.xlabel("Tid (dagar)")
plt.ylabel("Aktiekurs")

# Zomma in y-axeln för att visa variationen tydligare
plt.ylim(initial_price * 0.9, initial_price * 1.1)  # Exempel: zooma in till ±10% runt startkursen
plt.show()
