# 1216_회문2 풀이
# 2022-08-16

data = []
for tc in range(10):
    case = input()
    data.append([list(input()) for i in range(100)])

for tc in range(10):
    vtc_data = []
    for i in range(100):
        vtc_data.append([data[tc][j][i] for j in range(100)])
    max_len = 0
    for length in range(100):
        for i in range(100):
            for j in range(100 - length + 1):
                rev = data[tc][i][j:j + (length // 2)]
                if rev[::-1] == data[tc][i][j + ((length + 1) // 2):j + length]:
                    max_len = length
                    break
                rev = vtc_data[i][j:j + (length // 2)]
                if rev[::-1] == vtc_data[i][j + ((length + 1) // 2):j + length]:
                    max_len = length
                    break

    print('#{} {}'.format(tc + 1, max_len))

