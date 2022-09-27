# 5207_이진_탐색 풀이
# 2022-09-27

import sys
sys.stdin = open('sample_input.txt', 'r')


def binary_search(start, end, target):
    global flag
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == target:
            return 1
        if n_list[mid] < target:
            start = mid + 1
            if flag == -1:
                return 0
            else:
                flag = -1
        elif n_list[mid] > target:
            end = mid - 1
            if flag == 1:
                return 0
            else:
                flag = 1
    return 0


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    result = 0
    n_list.sort()
    for num in m_list:
        flag = 0
        result += binary_search(0, N - 1, num)
    print('#{} {}'.format(tc + 1, result))
