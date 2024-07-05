# https://www.hackerrank.com/challenges/np-linear-algebra/

import numpy as np

N = int(input())
A = np.array([list(map(float, input().split())) for _ in range(N)])
det_A = np.linalg.det(A)

# All this gibberish necessary only to meet the
# requirements of output on hackerrank.com
if int(det_A) == det_A:
    print(det_A)
else:
    print(f'{det_A:.2f}')
