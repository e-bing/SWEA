# 5205_퀵_정렬 풀이
# 2022-09-27

import sys
sys.stdin = open('sample_input.txt', 'r')


def quicksort(data, left, right):
    if left < right:
        new = partition(data, left, right)
        quicksort(data, left, new - 1)
        quicksort(data, new + 1, right)


def partition(data, left, right):
    pivot = data[left]
    i = left
    j = right
    while i <= j:
        while i <= j and data[i] <= pivot:
            i += 1
        while i <= j and data[j] >= pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    data[left], data[j] = data[j], data[left]
    return j


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    quicksort(numbers, 0, N - 1)
    print('#{}'.format(tc + 1), numbers[N // 2])