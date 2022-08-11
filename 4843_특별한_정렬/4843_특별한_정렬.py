# 4843_특별한_정렬 풀이
# 2022-08-11

T = int(input())
N = []
data = []
for tc in range(T):
    N.append(int(input()))
    data.append(list(map(int, input().split())))

for tc in range(T):
    i = 0
    while i < N[tc] - 1:
        if data[tc][i] < data[tc][i + 1]:
            data[tc][i], data[tc][i + 1] = data[tc][i + 1], data[tc][i]
            i = 0
        else:
            i += 1
    result = [0] * N[tc]
    for i in range(N[tc]):
        if i * 2 < N[tc]:
            result[i * 2] = data[tc][i]
        else:
            result[2 * (N[tc] - i) - 1] = data[tc][i]
    print('#{} ' .format(tc + 1), end='')
    print(*result[0:10])
