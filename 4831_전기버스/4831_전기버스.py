# 4831_전기버스 풀이
# 2022-08-09

T = int(input())
k_list = []
n_list = []
m_list = []
bus_stops = []
for tc in range(T):
    K, N, M = map(int, input().split())
    k_list.append(K)
    n_list.append(N)
    m_list.append(M)
    bus_stops.append([0] + list(map(int, input().split())) + [N])

for tc in range(T):
    flag = 0
    result = 0

    for i in range(m_list[tc] + 1):
        if bus_stops[tc][i + 1] - bus_stops[tc][i] > k_list[tc]:
            flag = 1
    if flag:
        pass
    else:
        remain = k_list[tc]
        for i in range(m_list[tc] + 1):
            if bus_stops[tc][i + 1] - bus_stops[tc][i] > remain:
                result += 1
                remain = k_list[tc]
            remain -= bus_stops[tc][i + 1] - bus_stops[tc][i]
    print('#{} {}' .format(tc+1, result))
