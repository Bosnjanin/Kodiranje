# Metoda_Najmanjih_Kvadrata.py
# Autor: Davud Bektaš
# Opis: Primjena metode najmanjih kvadrata za aproksimaciju podataka

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. GENERIRANJE PODATAKA
# ------------------------------
np.random.seed(0)
x = np.linspace(0, 10, 20)
y_true = 3 * x + 5
y = y_true + np.random.normal(scale=4, size=len(x))  # dodavanje šuma

# ------------------------------
# 2. LINEARNA REGRESIJA (y = a*x + b)
# ------------------------------
X_lin = np.vstack([x, np.ones(len(x))]).T  # Dizajnerska matrica za linearnu funkciju
params_lin = np.linalg.inv(X_lin.T @ X_lin) @ X_lin.T @ y
a, b = params_lin
print(f"Linearna aproksimacija: y = {a:.2f}x + {b:.2f}")

# ------------------------------
# 3. KVADRATNA REGRESIJA (y = ax^2 + bx + c)
# ------------------------------
X_quad = np.vstack([x**2, x, np.ones(len(x))]).T
params_quad = np.linalg.inv(X_quad.T @ X_quad) @ X_quad.T @ y
a2, b2, c2 = params_quad
print(f"Kvadratna aproksimacija: y = {a2:.2f}x² + {b2:.2f}x + {c2:.2f}")

# ------------------------------
# 4. CRTANJE REZULTATA
# ------------------------------
x_dense = np.linspace(0, 10, 400)
y_lin_fit = a * x_dense + b
y_quad_fit = a2 * x_dense**2 + b2 * x_dense + c2

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', label='Podaci (sa šumom)')
plt.plot(x_dense, y_lin_fit, color='blue', label='Linearni fit')
plt.plot(x_dense, y_quad_fit, color='red', linestyle='--', label='Kvadratni fit')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metoda Najmanjih Kvadrata')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
