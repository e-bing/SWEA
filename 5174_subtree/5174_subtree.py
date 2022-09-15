# 5174_subtree 풀이
# 2022-09-15

import sys
sys.stdin = open('sample_input.txt', 'r')


def order(n):
    global result
    if n:
        result += 1
        order(ch1[n])
        order(ch2[n])


T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    result = 0
    for i in range(E):
        if ch1[data[2 * i]]:
            ch2[data[2 * i]] = data[2 * i + 1]
        else:
            ch1[data[2 * i]] = data[2 * i + 1]
    order(N)
    print('#{} {}'.format(tc + 1, result))
