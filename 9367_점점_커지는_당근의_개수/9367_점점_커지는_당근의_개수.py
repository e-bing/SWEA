# 9367_점점_커지는_당근의_개수 풀이
# 2022-08-12

T = int(input())
num = []
carrots = []
for tc in range(T):
    num.append(int(input()))
    carrots.append(list(map(int, input().split())))
for tc in range(T):
    max_count = 0
    cnt = 1
    for i in range(1, num[tc]):
        if carrots[tc][i - 1] < carrots[tc][i]:
            cnt += 1
        else:
            if max_count < cnt:
                max_count = cnt
            cnt = 1
    if max_count < cnt:
        max_count = cnt
    print('#{} {}'.format(tc + 1, max_count))
