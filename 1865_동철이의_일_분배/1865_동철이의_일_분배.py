# 1865_동철이의_일_분배 풀이
# 2022-09-27

import sys
sys.stdin = open('input.txt', 'r')


def find_solution(depth, percent):
    global N, max_value
    if percent <= max_value:
        return
    if depth == N - 1:
        idx = 0
        for i in range(N):
            if i not in choice:
                idx = i
        percent *= 0.01 * p_list[depth][idx]
        if percent > max_value:
            max_value = percent
        return
    for i in range(N):
        if i not in choice:
            choice[depth] = i
            find_solution(depth + 1, percent * 0.01 * p_list[depth][i])
            choice[depth] = -1


T = int(input())
for tc in range(T):
    N = int(input())
    p_list = [list(map(int, input().split())) for i in range(N)]
    choice = [-1] * N
    max_value = float('-inf')
    find_solution(0, 1)
    max_value *= 100
    print('#{} {:.6f}'.format(tc + 1, max_value))