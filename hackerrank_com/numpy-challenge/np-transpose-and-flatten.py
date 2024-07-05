# https://www.hackerrank.com/challenges/np-transpose-and-flatten/

import numpy as np

N, M = map(int, input().split())
arr = np.array([[int(x) for x in input().split(' ')] for _ in range(M)])
print(np.transpose(arr))
print(arr.flatten())
