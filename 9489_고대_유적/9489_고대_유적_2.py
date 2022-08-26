# 9489_고대_유적
# 2022-08-26

import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(N)]
    max_value = 0
    for i in range(N):
        sum_value = 0
        for j in range(M):
            if data[i][j] == 1:
                sum_value += 1
            else:
                if sum_value > max_value:
                    max_value = sum_value
                sum_value = 0
        if sum_value > max_value:
            max_value = sum_value
    for i in range(M):
        sum_value = 0
        for j in range(N):
            if data[j][i] == 1:
                sum_value += 1
            else:
                if sum_value > max_value:
                    max_value = sum_value
                sum_value = 0
        if sum_value > max_value:
            max_value = sum_value
    print('#{} {}'.format(tc + 1, max_value))