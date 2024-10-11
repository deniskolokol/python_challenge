# https://www.hackerrank.com/challenges/most-commons/

from collections import Counter

def main(ln):
    counts_all = list(Counter(ln).items())
    counts_ordered = sorted(counts_all, key=lambda x: (-x[1], x[0]))
    for i in range(3):
        print("{0} {1}".format(*counts_ordered[i]))


if __name__ == '__main__':
    s = input()
    main(s)