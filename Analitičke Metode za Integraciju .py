#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 23:14:54 2025

@author: dawood_bektas
"""

# analiticka_matematika.py

import sympy as sp

def simbolicka_derivacija(f_expr, var):
    """
    Vraća simboličku derivaciju izraza f po varijabli var.
    
    Parametri:
        f_expr: sympy izraz (npr. sp.sin(x))
        var: simbol varijable (npr. x)

    Povrat:
        Derivacija izraza
    """
    return sp.diff(f_expr, var)

def simbolicka_integracija(f_expr, var):
    """
    Vraća simbolički integral izraza f po varijabli var.
    
    Parametri:
        f_expr: sympy izraz
        var: simbol varijable

    Povrat:
        Neodređeni integral izraza
    """
    return sp.integrate(f_expr, var)

def rjesavanje_ode(y, x, ode_expr):
    """
    Simboličko rješavanje obične diferencijalne jednadžbe (ODE).
    
    Parametri:
        y: funkcija (npr. sp.Function('y')(x))
        x: varijabla (npr. x)
        ode_expr: jednadžba u obliku izraza (npr. y.diff(x) + y - 1)

    Povrat:
        Opće rješenje ODE-a
    """
    return sp.dsolve(ode_expr, y)

if __name__ == "__main__":
    x = sp.symbols('x')
    f = sp.sin(x) * sp.exp(x)

    print("Derivacija:", simbolicka_derivacija(f, x))
    print("Integracija:", simbolicka_integracija(f, x))

    y = sp.Function('y')(x)
    ode = y.diff(x) + y - 1
    print("Rješenje ODE-a:", rjesavanje_ode(y, x, ode))
