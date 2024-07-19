# https://www.hackerrank.com/challenges/the-minion-game/


def minion_game(ln):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    for i in range(len(ln)):
        if ln[i] in vowels:
            kevin_score += len(ln) - i
        else:
            stuart_score += len(ln) - i

    if stuart_score == kevin_score:
        print('Draw')
    elif stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    else:
        print(f'Kevin {kevin_score}')


if __name__ == '__main__':
    s = input()
    minion_game(s)