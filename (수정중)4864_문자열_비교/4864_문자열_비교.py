# 4864_문자열_비교 풀이
# 2022-08-16

import sys
sys.stdin = open('sample_input.txt', 'r')

def find_idx(my_list, target):
    idx = 0
    for i in my_list:
        if i == target:
            return idx
        idx += 1
    return -1

T = int(input())
for tc in range(T):
    pattern = list(input())
    data = list(input())
    ptn_len = 0
    data_len = 0
    flag = 0
    skip_table = {}
    for i in pattern:
        ptn_len += 1
        if i not in skip_table.keys():
            skip_table[i] = ptn_len
    for i in skip_table:
        skip_table[i] = ptn_len - skip_table[i]
    for i in data:
        data_len += 1
    data_idx = ptn_len - 1
    while data_idx < data_len:
        for i in range(ptn_len):
            if pattern[ptn_len - i - 1] != data[data_idx - i]:
                if data[data_idx - i] not in skip_table.keys():
                    data_idx += ptn_len
                else:
                    data_idx += skip_table[data[data_idx - i]]
                break
            elif i == ptn_len - 1:
                flag = 1
                break
        if flag:
            break
    print('#{} {}'.format(tc + 1, flag))