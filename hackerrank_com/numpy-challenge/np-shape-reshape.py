# https://www.hackerrank.com/challenges/np-shape-reshape/

import numpy as np

ints = input().strip().split(' ')
print(np.array(ints, dtype=np.int16).reshape((3, 3)))
