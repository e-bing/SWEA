# 연습문제1_Gravity 풀이
# 2022-08-08

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(T):
    max = 0
    n = int(input())
    box = list(map(int, input().split()))

    for j in range(n):
        result = n - j
        for k in range(j, n):
            if box[k] >= box[j]:
                result -= 1

        if max < result:
            max = result

    print('#{} {}' .format(i + 1, max))