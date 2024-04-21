# Defino la librerias a utilizar
import numpy as np
import matplotlib.pyplot as plt

#Este comando indica que de la libreria math importe solamente el numero pi y no todo lo que contiene
from math import pi 

# Defino un rango de valores en radianes
radianes = np.arange(start=0, stop=4*pi, step=1/32 *pi)

# Funcion seno
seno_vector = [] #defino una lista vacia
for radian in radianes:
    valor_seno = np.sin(radian) #toma cada uno de los valores de "radianes" y calcula su seno
    seno_vector.append(valor_seno) #luego los ingresa a la lista creada al principio
seno_vector = np.array(seno_vector) #convierto la lista en un vector para graficarla

# Funcion coseno
coseno_vector = []
for radian in radianes:
    valor_coseno = np.cos(radian)
    coseno_vector.append(valor_coseno)
coseno_vector = np.array(coseno_vector)

#         eje x      eje y
plt.plot(radianes,seno_vector, "b")
plt.plot(radianes,coseno_vector, "y")
plt.show()