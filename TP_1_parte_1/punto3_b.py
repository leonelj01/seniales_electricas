import numpy as np

#Defino los rangos a graficar
positivos = np.linspace(start=0, stop=10, num=11, dtype='int')
enteros = np.linspace(start=-4, stop=2, num=7, dtype='int')
multiplos = np.arange(start=0, stop=14, step=3)
reverso = np.arange(start=10, stop=0, step=-1.5)

# Utilizo la libreria mathplotlib
import matplotlib.pyplot as plt

#grafico positivos
plt.plot(positivos, 'o')
plt.show()

#grafico enteros
plt.plot(enteros)
plt.show()

#grafico multiplos
plt.plot(multiplos)
plt.show()

#grafico reverso
plt.plot(reverso, 'x')
plt.show()

#grafico positivos y reverso en mismo plot
plt.plot(positivos, "bo")
plt.plot(reverso, "rx")
plt.show()