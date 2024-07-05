# https://www.hackerrank.com/challenges/np-array-mathematics/

import numpy as np

N, M = map(int, input().split())
arrA = np.array([[int(x) for x in input().split(' ')] for _ in range(N)])
arrB = np.array([[int(x) for x in input().split(' ')] for _ in range(N)])

print(arrA + arrB)
print(arrA - arrB)
print(arrA * arrB)
print(np.floor_divide(arrA, arrB))
print(np.mod(arrA, arrB))
print(np.power(arrA, arrB))
