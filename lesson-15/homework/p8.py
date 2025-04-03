import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.random.randint(10, 50, (3, 4))
fig, ax = plt.subplots()
bottom = np.zeros(4)
colors = ['red', 'blue', 'green']
for i, (category, color) in enumerate(zip(categories, colors)):
    ax.bar(time_periods, data[i], bottom=bottom, label=category, color=color)
    bottom += data[i]
ax.set_xlabel('Time Periods')
ax.set_ylabel('Value')
ax.set_title('Stacked Bar Chart')
ax.legend()
plt.show()