# 5209_최소_생산_비용 풀이
# 2022-09-27

import sys
sys.stdin = open('sample_input.txt', 'r')


def find_sol(depth, sum_value):
    global min_value, N
    if sum_value >= min_value:
        return
    if depth == N - 1:
        idx = 0
        for i in range(N):
            if i not in choice:
                idx = i
        sum_value += factories[depth][idx]
        if sum_value < min_value:
            min_value = sum_value
        return
    for i in range(N):
        if i not in choice:
            choice[depth] = i
            sum_value += factories[depth][i]
            find_sol(depth + 1, sum_value)
            sum_value -= factories[depth][i]
            choice[depth] = -1


T = int(input())
for tc in range(T):
    N = int(input())
    factories = [list(map(int, input().split())) for i in range(N)]
    choice = [-1] * N
    min_value = float('inf')
    find_sol(0, 0)
    print('#{} {}'.format(tc + 1, min_value))
