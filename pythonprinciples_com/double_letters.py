"""
Double letters.

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""

# Solution 1.
def double_letters(line):
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            return True

    return False


# Solution 2.
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])
