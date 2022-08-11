# 4837_부분집합의_합 풀이
# 2022-08-11

T = int(input())
A = [i for i in range(1, 13)]
n_list = []
k_list = []
for tc in range(T):
    N, K = map(int, input().split())
    n_list.append(N)
    k_list.append(K)
for tc in range(T):
    result = 0
    for i in range(1 << 12):
        sum_value = 0
        count_value = 0
        for j in range(12):
            if i & (1 << j):
                count_value += 1
                sum_value += A[j]
        if count_value == n_list[tc] and sum_value == k_list[tc]:
            result += 1
    print('#{} {}' .format(tc + 1, result))
