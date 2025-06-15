# Laplaceova_Transformacija.py
# Autor: Davud Bektaš
# Opis: Primjeri Laplaceove transformacije, inverzne transformacije i rješavanja ODE-a

import sympy as sp

# Definicija varijabli
t, s = sp.symbols('t s')
f = sp.Function('f')


# 1. LAPLACEOVA TRANSFORMACIJA

print("=== Laplaceova Transformacija ===")
f1 = sp.sin(t)
laplace_f1 = sp.laplace_transform(f1, t, s, noconds=True)
print(f"Laplace[sin(t)] = {laplace_f1}\n")

f2 = t**2
laplace_f2 = sp.laplace_transform(f2, t, s, noconds=True)
print(f"Laplace[t^2] = {laplace_f2}\n")


# 2. INVERZNA LAPLACEOVA

print("=== Inverzna Laplaceova Transformacija ===")
F1 = 1 / (s**2 + 1)
inv_f1 = sp.inverse_laplace_transform(F1, s, t)
print(f"Inverse Laplace[1 / (s^2 + 1)] = {inv_f1}\n")

F2 = s / (s**2 + 4)
inv_f2 = sp.inverse_laplace_transform(F2, s, t)
print(f"Inverse Laplace[s / (s^2 + 4)] = {inv_f2}\n")


# 3. RJEŠAVANJE ODE-a KORISTEĆI LAPLACE

print("=== Rješavanje ODE-a korištenjem Laplaceove transformacije ===")
# Jednadžba: f''(t) + 3f'(t) + 2f(t) = 0, f(0) = 1, f'(0) = 0
F = sp.Function('F')

f_t = f(t)
f_lap = sp.laplace_transform(f_t, t, s, noconds=True)

# Definiraj jednadžbu simbolički
f0 = 1  # f(0)
df0 = 0 # f'(0)

# Laplace[f''] = s^2*F(s) - s*f(0) - f'(0)
# Laplace[f'] = s*F(s) - f(0)
# Laplace[f] = F(s)

# ODE: s^2*F - s*f(0) - f'(0) + 3(s*F - f(0)) + 2*F = 0
F_s = sp.symbols('F', cls=sp.Function)
F_s = sp.Function('F')(s)
ode_laplace = s**2 * F_s - s*f0 - df0 + 3*(s*F_s - f0) + 2*F_s
ode_solved = sp.solve(ode_laplace, F_s)[0]

print(f"Laplaceova domena F(s) = {ode_solved}\n")

# Inverzna Laplaceova za F(s)
f_solution = sp.inverse_laplace_transform(ode_solved, s, t)
print(f"Rješenje u vremenskoj domeni f(t) = {f_solution}")


# 4. Tablica osnovnih transformacija (opcionalno)

print("\n=== Osnovne Laplaceove Transformacije ===")
basic_transforms = {
    "1": "1 / s",
    "t": "1 / s**2",
    "t^n": "n! / s^(n+1)",
    "e^(a*t)": "1 / (s - a)",
    "sin(ωt)": "ω / (s^2 + ω^2)",
    "cos(ωt)": "s / (s^2 + ω^2)"
}

for time_func, laplace_pair in basic_transforms.items():
    print(f"Laplace[{time_func}] = {laplace_pair}")



