import numpy as np
import math as mt


# Defino los vectores y matrices a utilizar
v = np.array([[1,3,7,0]])
w = np.array([[5],[6],[2]])
x = np.array([[0],[-2],[3],[7]])

M = w @ v
N = M @ x
P = np.transpose(w) @ M

# Realizo las funciones np.max, np.min y np.mean respectivamente

print(np.max(w))
print(np.min(x))
print(np.mean(v))

num = 3.14159570

print(round(num))

# round(num,n_digit) redondea el numero ingresado, si n_digit=none devuelve un numero entero y si ponemos un numero "x" redondeara el numero mostrando "x" digitos
# math.ceil(num) redondea el numero ingresado a su entero superior 
# abs(num) devuelve el valor absoluto del numero ingresado 