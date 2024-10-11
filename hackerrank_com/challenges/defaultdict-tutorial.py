# https://www.hackerrank.com/challenges/defaultdict-tutorial/

from collections import defaultdict


def get_indices(element, lst):
    offset = -1
    indices = []
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            if not indices:
                indices = [offset]
            return indices

        indices.append(offset+1)


n, m = map(int, input().split())
groups = defaultdict(list)
for _ in range(n):
    groups['A'].append(str(input()))
for _ in range(m):
    groups['B'].append(str(input()))

for elt in groups['B']:
    print(' '.join(map(str, get_indices(elt, groups['A']))))