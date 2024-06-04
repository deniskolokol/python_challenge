# https://www.hackerrank.com/challenges/np-arrays/

import numpy as np

def arrays(arr):
    return np.array(arr, dtype=np.float16)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
