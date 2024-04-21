import numpy as np
import matplotlib.pyplot as plt

# Crear una señal de ejemplo
t = np.linspace(0, 0.5, 500)
s = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)

# Aplicar la FFT
fft = np.fft.fft(s)

# Calcular las frecuencias para los valores de la FFT
T = t[1] - t[0]  # tiempo de muestreo
N = s.size
f = np.linspace(0, 1 / T, N)

# Graficar la señal original y la FFT
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Señal Original')

plt.subplot(2, 1, 2)
plt.plot(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N)  # 1 / N es una normalización
plt.title('Transformada de Fourier')

plt.tight_layout()
plt.show()
