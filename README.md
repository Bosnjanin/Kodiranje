Numeričke metode za rješavanje ODE-a

Ovaj repozitorij sadrži Python implementacije osnovnih numeričkih metoda za rješavanje običnih diferencijalnih jednadžbi (ODE).
Trenutno uključene metode:

Eulerova metoda

Heunova metoda (poboljšana Eulerova)

Runge-Kutta metoda četvrtog reda (RK4)

Također uključuje usporedni prikaz rezultata u odnosu na točno rješenje.

Zahtjevi:

Python 3.x

NumPy

Matplotlib

Instalacija potrebnih paketa (ako već nisu instalirani):

pip install numpy matplotlib 

Korištenje:

U datoteci ode_solvers.py, definirana je funkcija plot_euler_vs_exact koja uspoređuje tri numeričke metode s točnim rješenjem.

Primjer:

# Derivacija: dy/dx = -2y
# Točno rješenje: y(x) = e^(-2x)

Cilj:

Ovaj projekt je nastao kao edukacijski alat za učenje i podučavanje numeričkih metoda kroz praktične Python primjere.

Planiramo proširiti projekt s:

Višim redovima ODE-a

Sustavima diferencijalnih jednadžbi

Implicitnim metodama

Primjenama u inženjerstvu i fizici

Autor:

Dawood Bektaš

Za prijedloge, pitanja ili doprinos slobodno otvorite issue ili pull request!
