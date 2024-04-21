import numpy as np
import matplotlib.pyplot as plt
from math import pi

numeros_de_ciclos = 5
puntos_por_ciclo = 250

frecuencia = 20 #Hz

amplitud = 1

vector_tiempo_de_muestreo = np.linspace(start=0, stop= numeros_de_ciclos * (1/frecuencia), num=int(numeros_de_ciclos*puntos_por_ciclo))

senial_seno = []
w = 2 * pi * frecuencia
for  tiempo in vector_tiempo_de_muestreo:
    valor_seno = amplitud * np.sin(w*tiempo)
    senial_seno.append(valor_seno)
senial_seno = np.array(senial_seno)

senial_cuadrada = []
for muestra_seno in senial_seno:
    if muestra_seno > 0:
        valor_cuadrado = amplitud
    elif muestra_seno < 0:
        valor_cuadrado = -amplitud
    else:
        valor_cuadrado = 0
    senial_cuadrada.append(valor_cuadrado)
senial_cuadrada = np.array(senial_cuadrada)

plt.plot(vector_tiempo_de_muestreo,senial_seno)
plt.plot(vector_tiempo_de_muestreo,senial_cuadrada)
plt.xlabel("Tiempo [S]")
plt.ylabel("f(x)")
plt.show()