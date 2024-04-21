import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# Definir el tiempo de muestreo
t = np.linspace(0, 1, 500, endpoint=False)

# Crear una señal cuadrada con un ciclo de trabajo del 50%
square_wave = square(2 * np.pi * 5 * t)

# Aplicar la FFT a la señal cuadrada
fft = np.fft.fft2(square_wave)

# Calcular las frecuencias para los valores de la FFT
T = t[1] - t[0]  # tiempo de muestreo
N = square_wave.size
f = np.linspace(0, 1 / T, N)

# Graficar la señal cuadrada y su FFT
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t, square_wave)
plt.title('Señal Cuadrada')

plt.subplot(2, 1, 2)
plt.plot(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N)  # 1 / N es una normalización
plt.title('Transformada de Fourier')

plt.tight_layout()
plt.show()
