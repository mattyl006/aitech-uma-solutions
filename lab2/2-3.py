from mpl_toolkits.mplot3d import Axes3D  # niezbędne do rysowania powierzchni w 3 wymiarach
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)  # wygenerowanie tablicy danych wejściowych dla wykresu trójwymiarowego

Z = -(X**2 + Y**3) 

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=True)

plt.show()
