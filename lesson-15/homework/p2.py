import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), 'r--', label='sin(x)')
plt.plot(x, np.cos(x), 'b-', label='cos(x)')
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Sine and Cosine Plot')
plt.legend()
plt.grid()
plt.show()