import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label='f(x) = x^2 - 4x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Basic Plotting')
plt.legend()
plt.grid()
plt.show()
