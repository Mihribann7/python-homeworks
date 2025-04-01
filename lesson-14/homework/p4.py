import numpy as np

A_currents = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

B_currents = np.array([12, -5, 15])

currents = np.linalg.solve(A_currents, B_currents)
print(f"I1 = {currents[0]}, I2 = {currents[1]}, I3 = {currents[2]}")