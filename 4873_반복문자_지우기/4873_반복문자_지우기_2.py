# 4873_반복문자_지우기 풀이
# 2022-08-18

T = int(input())
for tc in range(T):
    data = list(input())
    length = 0
    idx = 0
    for i in data:
        length += 1
    while idx < length - 1:
        if data[idx] == data[idx + 1]:
            del data[idx]
            del data[idx]
            length -= 2
            if idx < 2:
                idx = 0
            else:
                idx -= 2
        else:
            idx += 1
    print('#{} {}'.format(tc + 1, length))