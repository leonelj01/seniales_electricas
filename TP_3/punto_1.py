import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definir el tiempo de muestreo
t = np.linspace(0, 1, 500, endpoint=True)

# Generar la señal cuadrada
senal_cuadrada = signal.square(2 * np.pi * 5 * t)

cuadrada = []
for signal in senal_cuadrada:
    if signal == 1:
        valor_cuad = 1
    else:
        valor_cuad = 0
    cuadrada.append(valor_cuad)
cuadrada = np.array(cuadrada)

# Graficar la señal cuadrada
plt.plot(t, cuadrada)
plt.show()
