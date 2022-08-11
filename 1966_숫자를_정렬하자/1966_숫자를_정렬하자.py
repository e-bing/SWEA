# 1966_숫자를_정렬하자 풀이
# 2022-08-11

T = int(input())
N = []
num_list = []
for tc in range(T):
    N.append(int(input()))
    num_list.append(list(map(int, input().split())))

for tc in range(T):
    i = 0
    while i < N[tc] - 1:
        if num_list[tc][i] > num_list[tc][i + 1]:
            num_list[tc][i], num_list[tc][i + 1] = num_list[tc][i + 1], num_list[tc][i]
            i = 0
        else:
            i += 1
    print('#{}'.format(tc + 1), end=' ')
    print(*num_list[tc])