# 1206_view 풀이
# 2022-08-08

import sys
sys.stdin = open('input.txt', 'r')

def check_buildings(buildings):
    max = 0
    for i in range(5):
        if i == 2:
            continue
        else:
            if buildings[i] >= buildings[2]:
                return 0
            elif max < buildings[i]:
                max = buildings[i]
    return buildings[2] - max

for tc in range(1, 10+1):
    T = int(input())
    # test 다 받아오기
    buildings = list(map(int, input().split()))
    # 문제 풀기
    result = 0
    for i in range(2, T - 2):
        result += check_buildings(buildings[i-2:i+3])
    print('#{} {}' .format(tc, result))