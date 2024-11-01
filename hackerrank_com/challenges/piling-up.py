# https://www.hackerrank.com/challenges/piling-up/


def pile_up(cubes):
    base = sum(cubes)
    while cubes:
        head, tail = cubes[0], cubes[-1]
        elt = max(head, tail)
        if elt <= base:
            if elt == tail:
                base = cubes.pop()
            else:
                base = cubes.pop(0)
            continue

        return False
    return True


def main():
    T = int(input())
    blocks = []
    for _ in range(T):
        size_ = int(input())
        blocks.append([int(x) for x in input().split(' ')])

    for cubes in blocks:
        if pile_up(cubes):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()