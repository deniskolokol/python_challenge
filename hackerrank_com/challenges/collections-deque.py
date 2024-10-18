# https://www.hackerrank.com/challenges/py-collections-deque/

import collections

N = int(input())
deq = collections.deque()
report = []
for ln in range(N):
    instr = input()
    arg = None
    try:
        command, arg = instr.split(' ')
    except ValueError:
        command = instr
    finally:
        command = command.strip()
    method = getattr(deq, command.strip())

    if arg:
        _ = method(arg)
    else:
        _ = method()

print(' '.join(deq))