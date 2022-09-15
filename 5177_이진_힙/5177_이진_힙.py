# 5177_이진_힙 풀이
# 2022-09-15

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    node = {}
    result = 0
    for i in range(N):
        node[i + 1] = data[i]
        cur = i + 1
        while (cur // 2 > 0) and node[cur // 2] > node[cur]:
            node[cur // 2], node[cur] = node[cur], node[cur // 2]
            cur = cur // 2
    N = N // 2
    while N > 0:
        result += node[N]
        N = N // 2
    print('#{} {}'.format(tc + 1, result))

