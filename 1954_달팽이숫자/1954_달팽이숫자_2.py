# 1954_달팽이숫자 풀이
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(T):
    N = int(input())
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    num = 0
    cur = [0, -1]
    data = [[0 for i in range(N)] for j in range(N)]
    for i in range(2 * N - 1):
        for j in range(N - (i + 1) // 2):
            cur[0] += directions[i % 4][0]
            cur[1] += directions[i % 4][1]
            num += 1
            data[cur[0]][cur[1]] = num
    print('#{}'.format(tc + 1))
    for i in range(N):
        print(*data[i])