import numpy as np

# Defino los vectores y matrices a utilizar
v = np.array([[1,3,7,0]])
w = np.array([[5],[6],[2]])
x = np.array([[0],[-2],[3],[7]])

M = w @ v
N = M @ x
P = np.transpose(w) @ M

# Realizo las extracciones pedidas
print("El primer elmento del vector v es",v[0][0],"\n")
print("EL tercer elemento del vector v es",v[0][2],"\n")
print("El elemento ubicado en la 2da fila y 3era columna de la matriz M es",M[1][2],"\n")
print("El onceavo elemento de la matriz M es",M.item(10),"\n")