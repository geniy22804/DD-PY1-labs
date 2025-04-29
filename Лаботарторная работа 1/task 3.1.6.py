import numpy as np

a = np.arange(12).reshape(2, 3, 2)
index = np.unravel_index(9, a.shape)
print(index)