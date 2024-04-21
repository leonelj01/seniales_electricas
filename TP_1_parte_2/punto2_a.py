import numpy as np
import matplotlib.pyplot as plt

numeros_de_ciclos = 30
puntos_por_ciclos = 200

frecuencia = 15 # Hz

tiempo_muestras_1 = np.linspace(start=0, stop= numeros_de_ciclos * (1/frecuencia), num=int(numeros_de_ciclos*puntos_por_ciclos))

senial_dientes_de_sierra = []
for ciclos in range(numeros_de_ciclos):
    for punto in range(puntos_por_ciclos):
        valor_senial = punto % puntos_por_ciclos
        senial_dientes_de_sierra.append(valor_senial)
senial_dientes_de_sierra = np.array(senial_dientes_de_sierra)

plt.plot(tiempo_muestras_1,senial_dientes_de_sierra,"orange")
plt.xlabel("Tiempo [S]")
plt.ylabel("f(x)")
plt.show()