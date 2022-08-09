# 4835_구간합 풀이
# 2022-08-09

T = int(input())
n_list = []
m_list = []
num_list = []
for tc in range(T):
    N, M = map(int, input().split())
    n_list.append(N)
    m_list.append(M)
    num_list.append(list(map(int, input().split())))

for tc in range(T):
    num_sum = 0
    for i in range(m_list[tc]):
        num_sum += num_list[tc][i]
    sum_min = num_sum
    sum_max = num_sum
    for i in range(n_list[tc] - m_list[tc] + 1):
        num_sum = 0
        for j in range(i, i + m_list[tc]):
            num_sum += num_list[tc][j]
        if num_sum < sum_min:
            sum_min = num_sum
        if num_sum > sum_max:
            sum_max = num_sum

    print('#{} {}' .format(tc + 1, sum_max - sum_min))
