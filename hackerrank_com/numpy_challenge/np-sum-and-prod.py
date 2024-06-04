# https://www.hackerrank.com/challenges/np-sum-and-prod/

import numpy as np

N, M = map(int, input().split())
arr = np.array([[int(x) for x in input().split(' ')] for _ in range(N)])
print(np.prod(arr.sum(axis=0)))
