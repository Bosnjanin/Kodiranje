# numerical-methods-python/methods/ode_solvers.py

import numpy as np
import matplotlib.pyplot as plt

def euler_solver(f, x0, y0, h, n):
    """
    Rješava običnu diferencijalnu jednadžbu pomoću Eulerove metode.

    Parametri:
        f: funkcija, derivacija f(x, y)
        x0: float, početna vrijednost x
        y0: float, početna vrijednost y (tj. y(x0))
        h: float, veličina koraka
        n: int, broj koraka

    Povrat:
        xs: numpy niz x vrijednosti
        ys: numpy niz y vrijednosti
    """
    xs = np.zeros(n + 1)
    ys = np.zeros(n + 1)

    xs[0] = x0
    ys[0] = y0

    for i in range(n):
        ys[i + 1] = ys[i] + h * f(xs[i], ys[i])
        xs[i + 1] = xs[i] + h

    return xs, ys

def heun_solver(f, x0, y0, h, n):
    """
    Rješava ODE pomoću poboljšane Eulerove metode (Heunova metoda).

    Parametri:
        f: funkcija, derivacija f(x, y)
        x0: float, početni x
        y0: float, početni y
        h: float, veličina koraka
        n: int, broj koraka

    Povrat:
        xs: numpy niz x vrijednosti
        ys: numpy niz y vrijednosti
    """
    xs = np.zeros(n + 1)
    ys = np.zeros(n + 1)

    xs[0] = x0
    ys[0] = y0

    for i in range(n):
        k1 = f(xs[i], ys[i])
        k2 = f(xs[i] + h, ys[i] + h * k1)
        ys[i + 1] = ys[i] + h * (k1 + k2) / 2
        xs[i + 1] = xs[i] + h

    return xs, ys

def rk4_solver(f, x0, y0, h, n):
    """
    Rješava ODE koristeći Runge-Kutta metodu četvrtog reda.

    Parametri:
        f: funkcija, derivacija f(x, y)
        x0: float, početni x
        y0: float, početni y
        h: float, veličina koraka
        n: int, broj koraka

    Povrat:
        xs: numpy niz x vrijednosti
        ys: numpy niz y vrijednosti
    """
    xs = np.zeros(n + 1)
    ys = np.zeros(n + 1)

    xs[0] = x0
    ys[0] = y0

    for i in range(n):
        k1 = f(xs[i], ys[i])
        k2 = f(xs[i] + h/2, ys[i] + h*k1/2)
        k3 = f(xs[i] + h/2, ys[i] + h*k2/2)
        k4 = f(xs[i] + h, ys[i] + h*k3)
        ys[i + 1] = ys[i] + h * (k1 + 2*k2 + 2*k3 + k4) / 6
        xs[i + 1] = xs[i] + h

    return xs, ys

def plot_euler_vs_exact(f, exact_solution, x0, y0, h, n):
    """
    Prikazuje usporedbu između numeričkih metoda i točnog rješenja.

    Parametri:
        f: funkcija, derivacija f(x, y)
        exact_solution: funkcija, točno rješenje y(x)
        x0: float, početni x
        y0: float, početni y
        h: float, korak
        n: int, broj koraka
    """
    xs_euler, ys_euler = euler_solver(f, x0, y0, h, n)
    xs_heun, ys_heun = heun_solver(f, x0, y0, h, n)
    xs_rk4, ys_rk4 = rk4_solver(f, x0, y0, h, n)
    xs_exact = np.linspace(x0, x0 + n*h, 1000)
    ys_exact = exact_solution(xs_exact)

    plt.figure(figsize=(10, 6))
    plt.plot(xs_exact, ys_exact, label='Točno rješenje', color='green')
    plt.plot(xs_euler, ys_euler, 'o--', label="Eulerova metoda", color='blue')
    plt.plot(xs_heun, ys_heun, 's--', label="Heunova metoda", color='orange')
    plt.plot(xs_rk4, ys_rk4, 'd--', label="RK4 metoda", color='purple')
    plt.title("Numeričke metode i točno rješenje")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Derivacija: dy/dx = -2y
    def f(x, y):
        return -2 * y

    # Točno rješenje: y(x) = e^(-2x)
    def exact_y(x):
        return np.exp(-2 * x)

    # Parametri
    x0 = 0
    y0 = 1
    h = 0.1
    n = 20

    plot_euler_vs_exact(f, exact_y, x0, y0, h, n)
