# 1230_암호문3 풀이
# 2022-08-26

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N = int(input())
    original = list(map(int, input().split()))
    order_num = int(input())
    orders = list(input().split())
    idx = 0
    for order in range(order_num):
        if orders[idx] == 'I':
            x = int(orders[idx + 1])
            y = int(orders[idx + 2])
            s = list(map(int, orders[idx + 3: idx + 3 + y]))
            for i in range(y):
                original.insert(x + i, s[i])
            idx += 3 + y
        elif orders[idx] == 'D':
            x = int(orders[idx + 1])
            y = int(orders[idx + 2])
            for i in range(y):
                del original[x]
            idx += 3
        elif orders[idx] == 'A':
            y = int(orders[idx + 1])
            s = list(map(int, orders[idx + 1:idx + 1 + y]))
            for i in range(y):
                original.append(s[i])
            idx += y + 2
        else:
            print('error', *orders[idx:idx+5])
    print('#{}'.format(tc + 1), *original[0:10])

