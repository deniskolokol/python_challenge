# https://www.hackerrank.com/challenges/word-order/

import collections

N = int(input())
words = []
for ln in range(N):
    words.append(input().strip())

ct = collections.Counter(words)
print(len(ct))
print(' '.join(str(v) for k, v in ct.items()))