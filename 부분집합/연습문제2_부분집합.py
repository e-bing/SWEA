# 연습문제2_부분집합 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    sum_num = -1
    num_list = list(map(int, input().split()))
    for i in range(1 << 10):
        if sum_num == 0:
            break
        sum_num = -1
        for j in range(10):
            if i & (1 << j):
                sum_num += num_list[j]
    if sum_num == 0:
        result = 1
    else:
        result = 0
    print('#{} {}' .format(tc + 1, result))