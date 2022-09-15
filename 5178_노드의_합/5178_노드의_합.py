# 5178_노드의_합 풀이
# 2022-09-15

import sys
sys.stdin = open('sample_input.txt', 'r')


def order(n):
    global N
    if n <= N:
        x = order(2 * n)
        y = order(2 * n + 1)
        try:
            nodes[n]
        except KeyError:
            nodes[n] = x + y
        return nodes[n]
    return 0


T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    nodes = {}
    for i in range(M):
        a, b = map(int, input().split())
        nodes[a] = b
    order(L)
    print('#{} {}'.format(tc + 1, nodes[L]))

