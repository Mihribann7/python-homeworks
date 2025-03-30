import numpy as np
random_5x5 = np.random.random((5, 5))
norm_matrix = (random_5x5 - random_5x5.min()) / (random_5x5.max() - random_5x5.min())
print("Normalized Matrix:", norm_matrix)