import numpy as np
import matplotlib.pyplot as plt

cantidad_de_muestras = 100e4
distribucion_uniforme = np.random.rand(int(cantidad_de_muestras))
distribucion_normal = np.random.randn(int(cantidad_de_muestras))

plt.hist(distribucion_uniforme, bins=200, alpha=0.75, facecolor="b", density=True, histtype='step')
plt.xlabel("x")
plt.ylabel("p(x)")
plt.show()

plt.hist(distribucion_normal, bins=200, alpha=0.75, facecolor="r", density=True, histtype='step')
plt.xlabel("x")
plt.ylabel("p(x)")
plt.show()