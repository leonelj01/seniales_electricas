import numpy as np 
from math import pi
import matplotlib.pyplot as plt

amplitud = 1 # V
frecuencia = 10 # Hz 

numeros_de_ciclos = 100

frecuencia_de_muestreo = 100 * frecuencia

vector_tiempo_de_muestra = np.arange(start=0, stop=numeros_de_ciclos * (1/frecuencia), step=1/frecuencia_de_muestreo)

angulo = pi/2

senial_seno_1 = []
senial_seno_2 = []
w = 2 * pi * frecuencia
for tiempo_muestra in vector_tiempo_de_muestra:
    valor_seno_1 = amplitud * np.sin(w*tiempo_muestra)
    valor_seno_2 = amplitud * np.sin(w*tiempo_muestra + angulo)

    senial_seno_1.append(valor_seno_1)
    senial_seno_2.append(valor_seno_2)
senial_seno_1 = np.array(senial_seno_1)
senial_seno_2 = np.array(senial_seno_2)

plt.plot(vector_tiempo_de_muestra, senial_seno_1)
plt.plot(vector_tiempo_de_muestra, senial_seno_2)
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [V]")
plt.show()