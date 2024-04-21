import matplotlib.pyplot as plt
import numpy as np

# Definir los rangos de voltaje
voltaje = [-1, 1, 2]

# Definir las probabilidades correspondientes
probabilidad = [0.4, 0.2, 0.4]

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.stem(voltaje, probabilidad)
plt.title('Función de Densidad de Probabilidad p(x)')
plt.xlabel('Voltaje (x)')
plt.ylabel('p(x)')
plt.grid(True)
plt.show()
