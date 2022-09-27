# 5204_병합_정렬 풀이
# 2022-09-27

import sys
sys.stdin = open('sample_input.txt', 'r')


def merge_sort(data):
    length = len(data)
    if length == 1:
        return data
    mid = length // 2
    l_list = data[:mid]
    r_list = data[mid:]
    l_list = merge_sort(l_list)
    r_list = merge_sort(r_list)
    return merge(l_list, r_list, mid, length - mid)


def merge(left, right, len_left, len_right):
    global cnt
    result = [0] * (len_left + len_right)
    idx = 0
    l_idx, r_idx = 0, 0
    if left[-1] > right[-1]:
        cnt += 1
    while len_left > 0 or len_right > 0:
        if len_left > 0 and len_right > 0:
            if left[l_idx] <= right[r_idx]:
                result[idx] = left[l_idx]
                len_left -= 1
                l_idx += 1
            else:
                result[idx] = right[r_idx]
                len_right -= 1
                r_idx += 1
        elif len_left > 0:
            result[idx] = left[l_idx]
            len_left -= 1
            l_idx += 1
        elif len_right > 0:
            result[idx] = right[r_idx]
            len_right -= 1
            r_idx += 1
        idx += 1
    return result


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    rslt = merge_sort(numbers)
    print('#{} {} {}'.format(tc + 1, rslt[N//2], cnt))
