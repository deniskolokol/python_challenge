# https://www.hackerrank.com/challenges/compress-the-string/

from itertools import groupby

inp = input().strip()
result = [(len(list(g)), int(k)) for k, g in groupby(inp)]
print(' '.join([str(x) for x in result]))