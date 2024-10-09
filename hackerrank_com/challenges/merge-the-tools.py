# https://www.hackerrank.com/challenges/merge-the-tools/

def merge_the_tools(string_, k):
    substrings = (string_[n:n+k] for n in range(0, int(len(string_)), k))
    for substr in substrings:
        result = ''
        for x in substr:
            if x in result:
                continue
            result += x
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)