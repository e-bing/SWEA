# 4836_색칠하기 풀이
# 2022-08-11

T = int(input())
N = []
red = []
blue = []
for tc in range(T):
    red_temp = []
    blue_temp = []
    N.append(int(input()))
    for i in range(N[tc]):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                if color == 1:
                    red_temp.append([j, k])
                else:
                    blue_temp.append([j, k])
    red.append(red_temp)
    blue.append(blue_temp)

for tc in range(T):
    result = 0
    for i in red[tc]:
        if i in blue[tc]:
            result += 1

    print('#{} {}' .format(tc + 1, result))
