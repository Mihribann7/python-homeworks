import numpy as np

A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B = np.array([7, 4, 5])

solution = np.linalg.solve(A, B)
print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")