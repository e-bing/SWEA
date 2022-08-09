# 6485_삼성시의 버스노선
# 2022-08-09

T = int(input())
N = []
P = []
all_buses = []
all_stops = []
for tc in range(T):
    N.append(int(input()))
    bus_list = []
    for i in range(N[tc]):
        bus_list.append(list(map(int, input().split())))
    all_buses.append(bus_list)
    P.append(int(input()))
    stops = [] # list of bus stops
    for i in range(P[tc]):
        stops.append(int(input()))
    all_stops.append(stops)

for tc in range(T):
    result = [0] * P[tc]
    for i in range(N[tc]): # 버스 수만큼 반복
        for j in range(P[tc]):
            if all_buses[tc][i][0] <= all_stops[tc][j] <= all_buses[tc][i][1]:
                result[j] += 1

    print('#{}' .format(tc + 1), end='')
    for i in range(P[tc]):
        print(' {}' .format(result[i]), end='')
    print('')