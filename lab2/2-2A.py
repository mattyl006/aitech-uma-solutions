# Wykres danych wczytanych z pliku
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Zadanie 2.2A')

x = np.arange(0.0, 100.0, 0.1)
# s444498
y = (4 - 4) * x**2 + (9 - 5) * x + (8 - 6)
plt.plot(x, y, color = 'blue', lw=2)

plt.show()  # pokaż wykres
