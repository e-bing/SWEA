# 4880_토너먼트_카드게임 풀이
# 2022-08-22

import sys
sys.stdin = open('sample_input.txt', 'r')


def tournament(data, depth):
    if depth == 1:
        return find_winner(data)
    else:
        scope = data[-1][1] - data[0][1] + 1
        a = tournament(data[0:(scope + 1)//2], depth - 1)
        b = tournament(data[(scope + 1)//2:], depth - 1)
        return find_winner([a, b])


def find_winner(data):
    data_len = 0
    for i in data:
        data_len += 1
    if data_len < 2:
        return data[0]
    if data[0][0] == data[1][0]:
        return data[0]
    elif (data[0][0]) == 3 and (data[1][0] == 1):
        return data[1]
    elif (data[0][0]) == 1 and (data[1][0] == 3):
        return data[0]
    elif data[0][0] < data[1][0]:
        return data[1]
    else:
        return data[0]


T = int(input())
for tc in range(T):
    N = int(input())
    num_data = list(map(int, input().split()))
    data = [[num_data[i], i + 1] for i in range(N)]
    depth = 0
    while 2 ** depth < N:
        depth += 1
    result = tournament(data, depth)
    print('#{} {}'.format(tc + 1, result[1]))
