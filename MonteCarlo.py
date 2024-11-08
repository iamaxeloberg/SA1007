import numpy as np

NT = 10**3  # number of experiments
t_max = 58  # maximum travel time
t0 = 43     # deterministic travel time

t1 = np.random.uniform(0, 10, NT)  # random float number with 0 <= t1 < 10
t2 = np.random.uniform(0, 5, NT)   # random float number with 0 <= t2 < 5

t_tot = t0 + t1 + t2
print("Maximum travel time in sample:", np.max(t_tot))

# calculate 90% percentile in sample
t_opt = np.percentile(t_tot, 90)
print("Optimal travel time, with only 10% late arrivals:", t_opt)

# test: How many of the times do you arrive within the chosen time
s = sum(t_tot <= t_opt)
print("You arrive in time in", (s / NT) * 100, "% of the cases")
