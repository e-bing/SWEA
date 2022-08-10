# 1209_Sum 풀이
# 2022-08-10

num_list = []
for tc in range(10):
    T = int(input())
    tc_list = []
    for i in range(100):
        tc_list.append(list(map(int, input().split())))
    num_list.append(tc_list)

for tc in range(10):
    max_value = 0
    sum_left = sum_right = 0
    for i in range(100):
        sum_x = sum_y = 0
        for j in range(100):
            sum_x += num_list[tc][i][j]
            sum_y += num_list[tc][j][i]
        if max_value < sum_x:
            max_value = sum_x
        if max_value < sum_y:
            max_value = sum_y
        sum_left += num_list[tc][i][i]
        sum_right += num_list[tc][i][99 - i]
    if max_value < sum_left:
        max_value = sum_left
    if max_value < sum_right:
        max_value = sum_right
    print('#{} {}' .format(tc + 1, max_value))
