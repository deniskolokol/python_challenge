# https://www.hackerrank.com/challenges/collections-counter/

from collections import Counter

X = int(input())
shoe_size = map(int, input().split())
N = int(input())
purchases = []
for ln in range(N):
    purchases.append(tuple(map(int, input().split())))

shoe_size_available = Counter(shoe_size)
total = 0
for purch in purchases:
    try:
        total += purch[1] if shoe_size_available[purch[0]] > 0 else 0 
    except KeyError:
        continue
    else:
        shoe_size_available[purch[0]] -= 1

print(total)