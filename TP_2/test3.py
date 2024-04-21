import numpy as np
import matplotlib.pyplot as plt

# Valores de tensión y cantidad de muestras del histograma
tension_values = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
samples = np.array([200, 500, 1100, 1500, 1700, 2500, 1200, 700, 400, 200])

# Normalizar las muestras para obtener la función de densidad de probabilidad (FDP)
pdf = samples / samples.sum()

# Calcular la función de probabilidad acumulada (FPA)
cdf = np.cumsum(pdf)

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(tension_values, cdf, marker='o')
plt.title('Función de Probabilidad Acumulada')
plt.xlabel('Valor de Tensión [V]')
plt.ylabel('Probabilidad Acumulada')
plt.grid(True)
plt.show()
