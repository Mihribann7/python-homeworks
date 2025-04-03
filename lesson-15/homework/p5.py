import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='blue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
