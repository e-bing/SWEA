# 1861_정사각형_방 풀이
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')


def dfs(my_graph, v):
    global N
    num = 0
    visited = [0] * (N ** 2)
    stack = []
    stack.append(v) # 0 ~ N ** 2
    while stack:
        t = stack.pop(-1) # t == 0 ~ N ** 2
        if not visited[t]:
            visited[t] = True
            num += 1
            for i in my_graph[t]:
                if not visited[rooms[i]]:
                    stack.append(rooms[i])
    return num


T = int(input())
for tc in range(T):
    N = int(input())
    temp = [list(map(int, input().split())) for i in range(N)]
    rooms = {}
    graph = [[] for i in range(N ** 2)]
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    max_value = 0
    max_idx = N ** 2
    visit = 0
    for i in range(N ** 2):
        rooms[temp[i // N][i % N]] = i
    for i in range(N):
        for j in range(N):
            for k in range(4):
                n_i = i + direction[k][0]
                n_j = j + direction[k][1]
                if 0 <= n_i < N and 0 <= n_j < N and abs(temp[n_i][n_j] - temp[i][j]) == 1:
                    graph[i * N + j].append(temp[n_i][n_j])
    for i in range(0, N ** 2):
        visit = dfs(graph, i)
        if visit >= max_value:
            max_value = visit
            if temp[i // N][i % N] < max_idx:
                max_idx = temp[i // N][i % N]
    print('#{} {} {}'.format(tc + 1, max_idx, max_value))