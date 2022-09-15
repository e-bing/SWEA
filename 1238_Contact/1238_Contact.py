# 1238_Contact 풀이
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N, start = map(int, input().split())
    data = list(map(int, input().split()))
    dst = [[] for i in range(101)]
    cur = [start]
    visited = []
    for i in range(N // 2):
        dst[data[i * 2]].append(data[i * 2 + 1])
    while True:
        next_ct = []
        for i in cur:
            visited.append(i)
        for i in cur:
            for j in dst[i]:
                if j not in visited:
                    next_ct.append(j)
        if not next_ct:
            break
        else:
            cur = []
            for i in next_ct:
                cur.append(i)
    max_value = 0
    for i in cur:
        if i > max_value:
            max_value = i
    print('#{} {}'.format(tc + 1, max_value))
