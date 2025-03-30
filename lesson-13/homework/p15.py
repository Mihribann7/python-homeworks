import numpy as np
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", column_sums)
