# https://www.hackerrank.com/challenges/py-collections-ordereddict/

from collections import OrderedDict

N = int(input())
purchases = OrderedDict()
for ln in range(N):
    product, price = input().rsplit(' ', 1)
    purchases.setdefault(product, 0)
    purchases[product] += int(price)

for k, v in purchases.items():
    print(k, v)