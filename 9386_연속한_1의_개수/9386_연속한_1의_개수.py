# 9386_연속한_1의_개수 풀이
# 2022-08-12

T = int(input())
length = []
data = []
for tc in range(T):
    length.append(int(input()))
    data.append(list(map(int, input())))

for tc in range(T):
    max_count = 0
    cnt = 0
    for i in range(length[tc]):
        if data[tc][i] == 1:
            cnt += 1
        else:
            if max_count < cnt:
                max_count = cnt
                cnt = 0
    if max_count < cnt:
        max_count = cnt
    print('#{} {}'.format(tc + 1, max_count))