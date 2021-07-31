import csv
import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = []
y1 = []

for i in x:

    a = np.sin(i*np.pi*0.1)
    y.append(a)

for i in x:
    a = np.sin(i*np.pi*0.2)
    y1.append(a)

fig = plt.figure()

ax = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax.plot(x,y, color='r', marker='^')
ax2.plot(x,y1, color='y', marker='o')

ax.set_facecolor('lightgray')
ax.set_title('Gráfico de prueba')
ax.set_ylabel('Seno')
ax.set_xlabel('Secuencia')
ax.grid()

plt.show()

print('Funciona!')