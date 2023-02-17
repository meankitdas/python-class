import numpy as np

string = "Hello World"

arr = [1,90,2,3,6,7,8,9,10]

nparr = np.array(arr)

rev_operation = np.flip(list(string))

arr_rev = np.flip(nparr)

print(arr_rev)

rev_string = "".join(rev_operation)

print(rev_string)