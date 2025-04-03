import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, x**3, 'g')
axs[0, 0].set_title('x^3')
axs[0, 1].plot(x, np.sin(x), 'r')
axs[0, 1].set_title('sin(x)')
axs[1, 0].plot(x, np.exp(x), 'b')
axs[1, 0].set_title('e^x')
x_pos = np.linspace(0, 2, 100)
axs[1, 1].plot(x_pos, np.log(x_pos+1), 'm')
axs[1, 1].set_title('log(x+1)')
plt.tight_layout()
plt.show()