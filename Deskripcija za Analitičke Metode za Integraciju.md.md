Analitičke metode u matematici (Python + SymPy)

Ovaj repozitorij sadrži jednostavne, edukativne primjere simboličke matematike u Pythonu koristeći biblioteku sympy.
Svrha modula je olakšati razumijevanje osnovnih analitičkih metoda kroz računalnu realizaciju.

Funkcionalnosti

Simbolička derivacija — izvod funkcije po zadanoj varijabli.

Simbolička integracija — integral funkcije po zadanoj varijabli.

Rješavanje običnih diferencijalnih jednadžbi (ODE) — korištenjem dsolve metode iz SymPy-a.

Korištenje

from analiticka_matematika import simbolicka_derivacija, simbolicka_integracija, rjesavanje_ode
import sympy as sp

x = sp.symbols('x')
f = sp.sin(x) * sp.exp(x)

print("Derivacija:", simbolicka_derivacija(f, x))
print("Integracija:", simbolicka_integracija(f, x))

y = sp.Function('y')(x)
ode = y.diff(x) + y - 1
print("Rješenje ODE-a:", rjesavanje_ode(y, x, ode))

Zahtjevi

Python 3.x

SymPy

Instalacija:

pip install sympy

Cilj

Ovaj modul ima za cilj:

Učiniti analitičke metode razumljivijima kroz automatizirano računanje.

Pomoći studentima i edukatorima u učenju, predavanju i rješavanju matematičkih problema.

Planirani razvoj

Dodavanje Taylorovih redova

Laplaceova transformacija

Fourierova analiza

Rješavanje sustava diferencijalnih jednadžbi

Autor

Dawood Bektaš

Za sugestije, komentare ili suradnju, slobodno otvorite issue ili pošaljite pull request!

