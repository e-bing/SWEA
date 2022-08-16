# 4861_회문 풀이
# 2022-08-16

T = int(input())
data = []
N = []
M = []
for tc in range(T):
    temp_N, temp_M = map(int, input().split())
    N.append(temp_N)
    M.append(temp_M)
    data.append([list(input()) for i in range(temp_N)])

for tc in range(T):
    vtc_data = []
    for i in range(N[tc]):
        vtc_data.append([data[tc][j][i] for j in range(N[tc])])
    result = 0
    for i in range(N[tc]):
        for j in range(N[tc] - M[tc] + 1):
            rev = data[tc][i][j:j + (M[tc] // 2)]
            if rev[::-1] == data[tc][i][j + ((M[tc] + 1) // 2):j + M[tc]]:
                result = ''.join(data[tc][i][j:j + M[tc]])
                break
            rev = vtc_data[i][j:j + (M[tc] // 2)]
            if rev[::-1] == vtc_data[i][j + ((M[tc] + 1) // 2):j + M[tc]]:
                result = ''.join(vtc_data[i][j:j + M[tc]])
                break
        if result:
            break
    print('#{} {}'.format(tc + 1, result))

