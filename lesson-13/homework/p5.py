import numpy as np
random_10x10 = np.random.random((10, 10))
min_val, max_val = random_10x10.min(), random_10x10.max()
print("Min:", min_val, "Max:", max_val)