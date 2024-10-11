# https://www.hackerrank.com/challenges/py-collections-namedtuple/

from collections import namedtuple

N = int(input())
Student = namedtuple('Student', [x.strip() for x in input().split()])
students = [Student(*tuple(input().split())) for _ in range(N)]
print(sum([int(x.MARKS) for x in students]) / len(students))