Numerička integracija u Pythonu

Ovaj repozitorij sadrži implementacije osnovnih numeričkih metoda za aproksimaciju određenih integrala u Pythonu.
Korištene metode su prikladne za jednostavne i srednje složene probleme gdje točna integracija nije moguća ili je nepraktična.

Implementirane metode:

Trapezno pravilo: koristi linearne aproksimacije funkcije između svake dvije točke.

Simpsonovo pravilo (1/3): koristi kvadratne parabole za aproksimaciju funkcije, zahtijeva paran broj podintervala.

Metoda srednje točke: koristi vrijednosti funkcije u sredini svakog podintervala.

Korištenje:

from numerical_integration import trapezna_pravilo, simpson_pravilo, srednja_tocka
import numpy as np

def f(x):
    return np.sin(x)

a = 0
b = np.pi
n = 100

print("Trapezno:", trapezna_pravilo(f, a, b, n))
print("Simpsonovo:", simpson_pravilo(f, a, b, n))
print("Srednja točka:", srednja_tocka(f, a, b, n))

Zahtjevi

Python 3.x

NumPy

Instalacija:

pip install numpy

Cilj:

Cilj ovog modula je pružiti jednostavan, pregledan i edukativan alat za razumijevanje i usporedbu osnovnih numeričkih metoda integracije.
Pogodan je za studente inženjerstva, fizike i računarstva.

Autor:

Dawood Bektaš

Za pitanja i prijedloge slobodno se javite ili otvorite issue!
