import numpy as np


a = [1,92,90,39,5,6,22,50,70,99,100,101]

numpy_arr = np.reshape(a, (2,3,2))

b = [[1,2,3,4],[5,3,2,1]]

numpy_3d = np.reshape(b, (2,2,2))

print(numpy_arr)
print(numpy_3d)

