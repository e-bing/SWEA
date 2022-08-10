# 연습문제1_델타검색 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    row_col = int(input())
    num_list = []
    for row in range(row_col):
        num_list.append(list(map(int, input().split())))

    x_idx = [0, 0, -1, 1]
    y_idx = [-1, 1, 0, 0]
    result = 0
    for i in range(0, row_col):
        for j in range(0, row_col):
            for k in range(4):
                ni = i + x_idx[k]
                nj = j + y_idx[k]
                if (0 <= ni < row_col) and (0 <= nj < row_col):
                    if num_list[i][j] < num_list[ni][nj]:
                        result += num_list[ni][nj] - num_list[i][j]
                    else:
                        result += num_list[i][j] - num_list[ni][nj]

    print('#{} {}' .format(tc + 1, result))
