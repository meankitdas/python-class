import numpy as np

arr = [[1,6,7,3,5],[2,5,7,3,0]]

numpy_arr = np.array(arr)

numpy_rev_arr = np.fliplr(numpy_arr)

print(numpy_rev_arr)