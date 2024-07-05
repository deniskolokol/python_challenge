# https://www.hackerrank.com/challenges/map-and-lambda-expression/

# Warning: the following snippet is a set of one-liners that are much more
# efficient and readable (hackerrank insists on the pattern below).
N = int(input().strip())
fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
print(list(map(lambda x: pow(x, 3), (fib(x) for x in range(N)))))


# Accepted solution:

cube = lambda x: pow(x, 3)

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
    return [fib(x) for x in range(n)]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
