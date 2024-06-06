# https://www.hackerrank.com/challenges/np-dot-and-cross/

import numpy as np

N = int(input())
arr1 = np.array([list(map(int, input().split())) for _ in range(N)])
arr2 = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.dot(arr1, arr2))
