import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(-10,10,100)
y= np.linspace(-10,10,100)
X, Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
plt.contour(X,Y,Z, levels=10,cmap="RdYlBu")
plt.colorbar()
plt.show()
