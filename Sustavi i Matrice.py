#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 14:46:44 2025

@author: dawood_bektas
"""

import numpy as np

# -----------------------------
# Gaussova eliminacija bez pivotiranja
# -----------------------------
def gauss_eliminacija(A, b):
    """
    Rješava sustav linearnih jednadžbi Ax = b Gaussovom eliminacijom.
    """
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Eliminacija
    for i in range(n):
        for j in range(i+1, n):
            faktor = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - faktor * A[i, i:]
            b[j] = b[j] - faktor * b[i]

    # Supstitucija unazad
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

    return x

# -----------------------------
# Inverz matrice pomoću Gauss-Jordan metode
# -----------------------------
def inverz_matrice(A):
    """
    Vraća inverznu matricu koristeći Gauss-Jordanovu metodu.
    """
    n = A.shape[0]
    AI = np.hstack((A.astype(float), np.eye(n)))

    for i in range(n):
        AI[i] = AI[i] / AI[i, i]
        for j in range(n):
            if i != j:
                AI[j] = AI[j] - AI[j, i] * AI[i]

    return AI[:, n:]

# -----------------------------
# Matrična svojstva i operacije
# -----------------------------
def mat_info(A):
    """
    Ispisuje osnovne informacije o matrici.
    """
    print("Dimenzije:", A.shape)
    print("Rang:", np.linalg.matrix_rank(A))
    print("Determinanta:", np.linalg.det(A))
    print("Vlastite vrijednosti:", np.linalg.eigvals(A))

# -----------------------------
# Primjer korištenja
# -----------------------------
if __name__ == "__main__":
    A = np.array([[2, -1, 0], [1, 2, -1], [3, 1, 1]], dtype=float)
    b = np.array([1, 2, 3], dtype=float)

    print("Rješenje sustava (Gauss eliminacija):")
    print(gauss_eliminacija(A.copy(), b.copy()))

    print("\nInverzna matrica:")
    print(inverz_matrice(A))

    print("\nInformacije o matrici A:")
    mat_info(A)
