# 연습문제2_BabyGin 풀이
# 2022-08-08

def counting_sort(data):
    max = data[0]
    for i in data:
        if max < i:
            max = i

    counts = [0] * (max + 1)
    for i in data:
        counts[i] += 1
    for i in range(1, max + 1):
        counts[i] += counts[i - 1]

    temp = [0] * 6
    for i in range(6):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]
    return temp

def check(data):
    if data[0] == data[1] == data[2]:
        return True
    elif data[0] + 2 == data[1] + 1 == data[2]:
        return True
    else:
        return False

def check_two_runs(data):
    if data[0] + 2 == data[1] + 2 == data[2] + 1 == data[3] + 1 == data[4] == data[5]:
        return True
    else:
        return False

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    result = 0
    case_list = list(map(int, input()))
    sort_list = counting_sort(case_list)
    if check(sort_list[0:3]) and check(sort_list[3:6]):
        result = 1
    elif check_two_runs(sort_list):
        result = 1

    print('#{} {}' .format(i+1, result))
