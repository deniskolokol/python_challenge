# https://www.hackerrank.com/challenges/np-mean-var-and-std/

import numpy as np

N, M = map(int, input().split())
arr = np.array([[int(x) for x in input().split(' ')] for _ in range(N)])
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
std_ = np.std(arr)
if std_:
    print(f'{np.std(arr) :.11f}')
else:
    print(std_)
