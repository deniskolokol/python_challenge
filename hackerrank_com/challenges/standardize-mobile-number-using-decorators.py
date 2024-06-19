# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

import re

def wrapper(f):
    def fun(l):
        result = []
        for num in l:
            num = re.sub('[^0-9]', '', num)
            num = num[-10:]
            num = f'+91 {num[:5]} {num[5:]}'
            result.append(num)

        return f(result)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)