# https://www.hackerrank.com/challenges/np-polynomials/

import numpy as np

coeffs = np.array(list(map(float, input().split())))
x = int(input().strip())

print(np.polyval(coeffs, x))
