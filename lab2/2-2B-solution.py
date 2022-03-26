# Wykres danych wczytanych z pliku
from math import e
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# print (np.exp(2))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Zadanie 2.2B')

x = np.arange(0.0, 100.0, 0.1)
# s444498
y = (4 - 4) * x**2 + (9 - 5) * x + (8 - 6)
plt.plot(x, y, color = 'blue', lw=2)

g = e**x / (e**x + 1)

plt.plot(x, g, color = 'red', lw=2)

plt.show()  # pokaż wykres
