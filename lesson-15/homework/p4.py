import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c='purple', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.grid()
plt.show()