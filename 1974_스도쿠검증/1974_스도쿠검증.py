# 1974_스도쿠검증
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    sudoku = [list(map(int, input().split())) for i in range(9)]
    result = 1
    for line in range(9):
        for i in range(8):
            for j in range(i + 1, 9):
                if sudoku[line][i] == sudoku[line][j]:
                    result = 0
                    break
                elif sudoku[i][line] == sudoku[j][line]:
                    result = 0
                    break
                elif sudoku[(line // 3) * 3 + i // 3][(line % 3) * 3 + i % 3] == sudoku[(line // 3) * 3 + j // 3][(line % 3) * 3 + j % 3]:
                    result = 0
                    break
        if result == 0:
            break
    print('#{} {}'.format(tc + 1, result))

