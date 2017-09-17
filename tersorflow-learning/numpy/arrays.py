import numpy as np

# create a rank 1 array
a = np.array([1, 2, 3])
# print(type(a))
# print(a.shape)

# create a rank 2 array 2 * 3
b = np.array([[1, 2, 3],
              [4, 5, 6]
              ])
# print(b.shape)
# print(b[1, 1])  # 5

# other many functions to create arrays
c = np.zeros((2,))
# print(c)

d = np.ones((2, 2))
# print(d)

e = np.eye(2)
# print(e)

f = np.random.random((2, 2))
print(f)