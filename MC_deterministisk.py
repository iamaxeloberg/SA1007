# -*- coding: utf-8 -*-
import numpy as np

# Definiera funktionen f(x) = x^2
def f(x):
    return x ** 2

# Antal punkter att generera
num_points = 100000

# Generera slumpmässiga x- och y-värden mellan 0 och 1
x_random = np.random.rand(num_points)
y_random = np.random.rand(num_points)

# Räkna antalet punkter där y < f(x)
under_curve = y_random < f(x_random)
hits_under_curve = np.sum(under_curve)

# Approximation av integralen (arean under kurvan)
area = hits_under_curve / num_points

print(f"Approximativt värde på integralen: {area:.4f}")

