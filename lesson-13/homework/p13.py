import numpy as np
matrix_3x3 = np.random.random((3, 3))
vector_3 = np.random.random(3)
matrix_vector_product = np.dot(matrix_3x3, vector_3)
print("Matrix-Vector Product:", matrix_vector_product)