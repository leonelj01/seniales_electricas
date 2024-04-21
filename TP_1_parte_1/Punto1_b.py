import numpy as np

# Defino los vectores a utilizar, en este formato se consideran listas

v = [1,3,7,0]
w = [[5],[6],[2]]
x = [[0],[-2],[3],[7]]

# Los convierto en arreglos para poder trabajarlos como matrices

v = np.array(v)
w = np.array(w)
x = np.array(x)

# Realizo la transpuesta de X

x_transpuesta = np.transpose(x)

# Imprimo por patalla las matrices
print(v, "\n")
print(w, "\n")
print(x, "\n")
print(x_transpuesta,"\n")