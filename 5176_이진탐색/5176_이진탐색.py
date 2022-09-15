# 5176_이진탐색 풀이
# 2022-09-15

import sys
sys.stdin = open('sample_input.txt', 'r')


def order(n):
    global num
    if n:
        order(ch1[n])
        num += 1
        node[n] = num
        order(ch2[n])


T = int(input())
for tc in range(T):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    node = {}
    num = 0
    for i in range(1, N + 1):
        if 2 * i <= N:
            ch1[i] = 2 * i
        if 2 * i + 1 <= N:
            ch2[i] = 2 * i + 1
    order(1)
    print('#{} {} {}'.format(tc + 1, node[1], node[N // 2]))
