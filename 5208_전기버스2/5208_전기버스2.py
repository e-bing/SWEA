# 5208_전기버스2 풀이
# 2022-09-27

import sys
sys.stdin = open('sample_input.txt', 'r')


def find_solution(idx, depth):
    global min_value, N
    if (depth >= min_value) or (battery[idx] + idx >= N - 1):
        if min_value > depth:
            min_value = depth
        return
    for i in range(idx, idx + battery[idx]):
        find_solution(i + 1, depth + 1)


T = int(input())
for tc in range(T):
    data = list(map(int, input().split()))
    N = data[0]
    battery = data[1:]
    min_value = N - 1
    find_solution(0, 0)
    print('#{} {}'.format(tc + 1, min_value))
