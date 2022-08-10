# 1954_달팽이_숫자
# 2022-08-10

T = int(input())
length = []
for tc in range(T):
    length.append(int(input()))

for tc in range(T):
    direction = [-1, 1]
    idx = [0, -1]
    num = 1
    interval = length[tc]
    data = []
    for i in range(length[tc]):
        data.append([0] * length[tc])
    for i in range(length[tc] * 2 - 1):
        if i % 2:
            interval -= 1
            direction[0] *= -1
            direction[1] *= -1
        for j in range(interval):
            if i % 2:
                idx[0] += direction[0]
            else:
                idx[1] += direction[1]
            data[idx[0]][idx[1]] = num
            num += 1

    print('#{}' .format(tc + 1))
    for row in data:
        print(*row)