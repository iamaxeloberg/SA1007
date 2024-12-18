import numpy as np

def approximate_pi(num_terms):
    # Skapa en array med index k från 0 till num_terms-1
    k = np.arange(num_terms)
    
    # Använd Leibniz formel för att beräkna varje term i serien
    terms = (-1) ** k / (2 * k + 1)
    
    # Summa av alla termer multiplicerat med 4 ger approximation av pi
    pi_approximation = 4 * np.sum(terms)
    return pi_approximation

# Kör approximationen med ett valt antal termer
num_terms = 1000000
pi_value = approximate_pi(num_terms)
print(f"Approximation of π with {num_terms} terms: {pi_value}")
