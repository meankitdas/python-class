import numpy as np

arr = [1,2,3,4,5,6]

arr_num = np.array(arr)
a_rev = []

# print(arr_num[::-1])
a_rev = []

for i in arr_num:
    a = arr_num[len(arr_num)-i]
    a_rev.append(a)
   
print(a_rev)
