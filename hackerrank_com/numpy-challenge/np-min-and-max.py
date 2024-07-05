# https://www.hackerrank.com/challenges/np-min-and-max/

import numpy as np

N, M = map(int, input().split())
arr = np.array([[int(x) for x in input().split(' ')] for _ in range(N)])
print(np.min(arr, axis=1).max())
