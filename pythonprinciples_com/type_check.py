"""
Type check.

Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

WARNING: isinstance(x, int) won't work, because isinstance(True, int) == True
"""

# Solution 1.
def only_ints(x, y):
    return (type(x) == int) and (type(y) ==int)

# Solution 2: more general.
def only_ints(*args):
    return all(type(x) == int for x in args)
