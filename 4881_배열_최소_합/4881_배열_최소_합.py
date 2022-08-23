# 4881_배열_최소_합 풀이
# 2022-08-23

import sys
sys.stdin = open('sample_input.txt', 'r')


def backtrack(data, choice, N, top, min_value):
    if top == N:
        sum_value = 0
        for i in range(N):
            sum_value += data[i][choice[i]]
        return sum_value
    else:
        for num in range(N):
            if check(data, choice, num, top, min_value):
                choice.append(num)
                top += 1
                result = backtrack(data, choice, N, top, min_value)
                if (min_value == -1) or (min_value > result):
                    min_value = result
                choice.pop(-1)
                top -= 1
    return min_value


def check(data, choice, num, idx, min_value):
    sum_value = data[idx][num]
    for i in range(idx):
        sum_value += data[i][choice[i]]
        if choice[i] == num:
            return False
    if (min_value == -1) or (sum_value < min_value):
        return True
    else:
        return False


T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    choice = []
    result = backtrack(data, choice, N, 0, -1)
    print('#{} {}'.format(tc + 1, result))
