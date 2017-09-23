import numpy as np

a = np.array([1, 1, 1])[:, np.newaxis]
b = np.array([2, 2, 2])[:, np.newaxis]

c = np.vstack((a, b)) # vertical stack
d = np.hstack((a , b)) # horizontal


print(a)
