#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 23:02:08 2025

@author: dawood_bektas
"""

import numpy as np

def trapezna_pravilo(f, a, b, n):
    """
    Kompozitno trapezno pravilo za numeričku integraciju funkcije f na intervalu [a, b].

    Parametri:
        f: funkcija koju integriramo
        a: donja granica integracije
        b: gornja granica integracije
        n: broj podintervala

    Povrat:
        Približna vrijednost integrala
    """
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        suma += f(a + i * h)
    return h * suma

def simpson_pravilo(f, a, b, n):
    """
    Simpsonovo 1/3 pravilo za numeričku integraciju funkcije f na intervalu [a, b].

    Parametri:
        f: funkcija koju integriramo
        a: donja granica
        b: gornja granica
        n: broj podintervala (mora biti paran)

    Povrat:
        Približna vrijednost integrala
    """
    if n % 2 != 0:
        raise ValueError("Broj podintervala mora biti paran za Simpsonovo pravilo.")

    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        koef = 4 if i % 2 != 0 else 2
        suma += koef * f(a + i * h)
    return h * suma / 3

def srednja_tocka(f, a, b, n):
    """
    Pravilo srednje točke (Midpoint rule).

    Parametri:
        f: funkcija
        a, b: granice integracije
        n: broj podintervala

    Povrat:
        Približna vrijednost integrala
    """
    h = (b - a) / n
    suma = 0
    for i in range(n):
        xi = a + i * h
        xi_sredina = xi + h / 2
        suma += f(xi_sredina)
    return h * suma

if __name__ == "__main__":
    def f(x):
        return np.sin(x)

    a = 0
    b = np.pi
    n = 100

    print("Trapezno pravilo:", trapezna_pravilo(f, a, b, n))
    print("Simpsonovo pravilo:", simpson_pravilo(f, a, b, n))
    print("Srednja točka:", srednja_tocka(f, a, b, n))
