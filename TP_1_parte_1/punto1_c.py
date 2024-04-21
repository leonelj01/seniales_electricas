import numpy as np

# Defino las variables pedidas en el ejercicio anterior
a = 5
A = 7
b = 8.
B = 11

# Defino las matrices
v = np.array([[1,3,7,0]])
w = np.array([[5],[6],[2]])
x = np.array([[0],[-2],[3],[7]])

# a * A
print("\n a * A = ",a * A,"\n")

# v * x
print("\n v * x =" ,v @ x,"\n") # el @ funciona como producto vectorial

# x * v
print("\n x * v = \n",x @ v,"\n")

# M = w * v
M = w @ v
print("\n M = \n",M,"\n")

# v * w
# Esta operacion no es posible debido a que no se puede realizar el producto vectorial entre estos vectores
# Por ello, salta un error cuando Python lo intenta hacer.

# N = M * x
N = M @ x
print("\n N =\n",N,"\n")

# P = w' * M
P = np.transpose(w) @ M
print("\n P =",P,"\n")