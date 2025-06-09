#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 15:43:43 2025

@author: dawood_bektas
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Diskretna Fourierova Transformacija (DFT)
# -----------------------------
def dft(x):
    """
    Ručna implementacija DFT (za edukativne svrhe).
    Ulaz:
        x: niz stvarnih ili kompleksnih brojeva
    Povrat:
        niz Fourierovih koeficijenata
    """
    x = np.asarray(x, dtype=complex)
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# -----------------------------
# Brza Fourierova Transformacija (FFT)
# -----------------------------
def fft(x):
    """
    Rekurzivna implementacija FFT (Cooley-Tukey algoritam).
    """
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    if N <= 1:
        return x
    elif N % 2 != 0:
        raise ValueError("Duljina niza mora biti potencija od 2.")
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N // 2] * X_odd,
                               X_even - factor[:N // 2] * X_odd])

# -----------------------------
# Vizualizacija signala i spektra
# -----------------------------
def prikazi_signal_i_spektrum(x, naziv="Signal"):
    N = len(x)
    X = np.fft.fft(x)
    frekvencije = np.fft.fftfreq(N)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, label=naziv)
    plt.title(f"{naziv} u vremenu")
    plt.xlabel("Uzorci")
    plt.ylabel("Amplituda")
    plt.grid()
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.stem(frekvencije, np.abs(X), use_line_collection=True)
    plt.title("Frekvencijski spektar (|X(k)|)")
    plt.xlabel("Frekvencija")
    plt.ylabel("Amplituda")
    plt.grid()

    plt.tight_layout()
    plt.show()

# -----------------------------
# Primjer korištenja
# -----------------------------
if __name__ == "__main__":
    t = np.linspace(0, 1, 256, endpoint=False)
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

    print("Prikaz signala i FFT spektra...")
    prikazi_signal_i_spektrum(signal, naziv="Zbroj sinusoida")

    print("DFT i FFT rezultati se uspoređuju...")
    X_dft = dft(signal)
    X_fft = np.fft.fft(signal)
    print("Razlika između DFT i FFT (maksimalna razlika):")
    print(np.max(np.abs(X_dft - X_fft)))
