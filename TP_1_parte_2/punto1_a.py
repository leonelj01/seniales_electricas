import numpy as np
from math import pi
import matplotlib.pyplot as plt

numeros_de_ciclos = 100

# Señal 1
frec_1 = 20 #Hz
amp_1 = 3 # V

# Señal 2
frec_2 = 33.57 #Hz
amp_2 = 4 # V 

frec_muestreo = 100 * frec_2

vector_tiempo_de_muestra = np.arange(start=0, stop=numeros_de_ciclos * (1/frec_1), step=1/frec_muestreo)

# Realizo la señal 1
seno_1 = []
w_1 = 2 * pi * frec_1
for tiempo_muestra in vector_tiempo_de_muestra:
    valor_seno_1 = amp_1 * np.sin(w_1*tiempo_muestra) # A *sen(wt)
    seno_1.append(valor_seno_1)
seno_1 = np.array(seno_1)

# Realizo la señal 2
seno_2 = []
w_2 = 2 * pi *frec_2
for tiempo_muestra in vector_tiempo_de_muestra:
    valor_seno_2 = amp_2 * np.sin(w_2 * tiempo_muestra)
    seno_2.append(valor_seno_2)
seno_2 = np.array(seno_2)

# Muestro la señal
plt.plot(vector_tiempo_de_muestra, seno_1)
plt.plot(vector_tiempo_de_muestra, seno_2)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.show()

# Calculo de los valores eficaces
valor_eficaz_1 = amp_1 / np.sqrt(2)
print("\nEl valor eficaz 1 es", valor_eficaz_1)

valor_eficaz_2 = amp_2 / np.sqrt(2)
print("\nEl valor eficaz 2 es", valor_eficaz_2)

valor_eficaz_suma = np.sqrt(valor_eficaz_1**2 + valor_eficaz_2**2)
print("\nEl valor eficaz de la suma es:", valor_eficaz_suma)

# Calculo de los promedios estadisticos

desviacion_estandar_1 = np.std(seno_1)
print("\nDesviacion estadar 1: ", desviacion_estandar_1)

desviacion_estandar_2 = np.std(seno_2)
print("\nDesviacion estandar 2: ", desviacion_estandar_2)