# 4828_min-max 풀이
# 2022-08-09

T = int(input())

n_list = []
num_list = []
for tc in range(T):
    n_list.append(int(input()))
    num_list.append(list(map(int, input().split())))

for tc in range(T):
    min_num = num_list[tc][0]
    max_num = num_list[tc][0]
    for i in num_list[tc]:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i

    print('#{} {}' .format(tc + 1, max_num - min_num))