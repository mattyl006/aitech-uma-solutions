# Wykres danych wczytanych z pliku

import matplotlib.pyplot as plt
import pandas as pd

# Wczytanie danych
data = pd.read_csv('data2.csv')
data_array = data.to_numpy()

# Wybór kolumn do przedstawienia na wykresie
x = data_array[:, 1]
y = data_array[:, 2]

plt.plot(x, y, 'ro')  # "gx" - zielone (Green) krzyżyki (x)
#plt.axis([0, 10, 0, 10])  # opcjonalnie ustawiamy zakres osi wykresu

plt.show()  # pokaż wykres
