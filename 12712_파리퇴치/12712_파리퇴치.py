# 12712_파리퇴치
# 2022-08-26

import sys
sys.stdin = open('in1.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(N)]
    direction = [[[-1, 0], [1, 0], [0, -1], [0, 1]], [[-1, -1], [-1, 1], [1, -1], [1, 1]]]
    max_value = 0
    for cur_i in range(N):
        for cur_j in range(N):
            sum_value = [data[cur_i][cur_j], data[cur_i][cur_j]]
            for i in range(1, M):
                for direct in range(2):
                    for j in range(4):
                        n_i = cur_i + direction[direct][j][0] * i
                        n_j = cur_j + direction[direct][j][1] * i
                        if (0 <= n_i < N) and (0 <= n_j < N):
                            sum_value[direct] += data[n_i][n_j]
                    if max_value < sum_value[direct]:
                        max_value = sum_value[direct]
    print('#{} {}'.format(tc + 1, max_value))