import matplotlib.pyplot as plt
import numpy as np

# Definir los rangos de voltaje
voltaje = [-np.inf, -1, 1, 2, np.inf]

# Definir las probabilidades correspondientes
probabilidad = [0, 0.4, 0.6, 1, 1]

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.step(voltaje, probabilidad, where='post')
plt.title('Función de Probabilidad Acumulativa F(x)')
plt.xlabel('Voltaje (x)')
plt.ylabel('F(x)')
plt.grid(True)
plt.show()
