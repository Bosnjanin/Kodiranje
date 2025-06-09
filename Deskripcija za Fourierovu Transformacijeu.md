Fourierova Transformacija u Pythonu
Ovaj projekt demonstrira kako diskretna i brza Fourierova transformacija (DFT i FFT) mogu biti implementirane i primijenjene na analizu signala. Idealno za edukativne svrhe i uvod u frekvencijsku analizu.

Sadržaj
1. Diskretna Fourierova Transformacija (DFT)
Ručno implementirana verzija koristeći definicijsku formulu.

Korisna za razumijevanje temelja frekvencijske dekompozicije.

2. Brza Fourierova Transformacija (FFT)
Efikasna rekurzivna implementacija Cooley-Tukey algoritma.


3. Vizualizacija
Prikaz originalnog signala u vremenskoj domeni.

Prikaz amplitudnog spektra u frekvencijskoj domeni.

Kako koristiti
Pokreni datoteku direktno:

bash
Copy
Edit
python fourier_transformacija.py

Izlaz će:

generirati i prikazati zbroj sinusoida kao testni signal

iscrtati pripadajući frekvencijski spektar

usporediti vlastitu implementaciju DFT s numpy FFT

Primjena
Ovaj projekt je koristan za:

studente elektrotehnike, računarstva i fizike

vizualnu demonstraciju kako se signal pretvara iz vremena u frekvenciju

edukaciju o efikasnosti FFT algoritma naspram ručne DFT metode

Ovisnosti
numpy

matplotlib

Instalacija:

bash
Copy
Edit
pip install numpy matplotlib
