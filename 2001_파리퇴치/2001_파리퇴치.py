# 2001_파리퇴치 풀이
# 2022-08-11

T = int(input())
n_list = []
m_list = []
flies = []
for tc in range(T):
    N, M = map(int, input().split())
    n_list.append(N)
    m_list.append(M)
    flies_temp = []
    for i in range(N):
        flies_temp.append(list(map(int, input().split())))
    flies.append(flies_temp)
for tc in range(T):
    max_value = 0
    for i in range(n_list[tc] - m_list[tc] + 1):
        for j in range(n_list[tc] - m_list[tc] + 1):
            sum_value = 0
            for k in range(m_list[tc]):
                for l in range(m_list[tc]):
                    sum_value += flies[tc][j + l][i + k]
            if sum_value > max_value:
                max_value = sum_value
    print('#{} {}' .format(tc + 1, max_value))