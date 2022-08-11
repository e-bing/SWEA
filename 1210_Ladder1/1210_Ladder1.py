# 1210_Ladder1 풀이
# 2022-08-11

SIZE = 100

ladder = []
for tc in range(10):
    temp_ladder = []
    T = int(input())
    for i in range(SIZE):
        temp_ladder.append(list(map(int, input().split())))
    ladder.append(temp_ladder)

for tc in range(10):
    for i in range(SIZE):
        if ladder[tc][99][i] == 2:
            x_idx = i
    for idx in range(SIZE):
        if (1 <= x_idx) and (ladder[tc][99 - idx][x_idx - 1] == 1):
            while (1 <= x_idx) and (ladder[tc][99 - idx][x_idx - 1] == 1):
                x_idx -= 1
        elif (x_idx < SIZE - 1) and (ladder[tc][99 - idx][x_idx + 1] == 1):
            while (x_idx < SIZE - 1) and (ladder[tc][99 - idx][x_idx + 1] == 1):
                x_idx += 1
    print('#{} {}' .format(tc + 1, x_idx))
