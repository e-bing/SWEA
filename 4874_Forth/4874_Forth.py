# 4874_Forth 풀이
# 2022-08-23

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(T):
    data = list(input().split())
    num = []
    top = -1
    flag = 1
    for i in data:
        if i == '+':
            if top > 0:
                num.append(num.pop(-1) + num.pop(-1))
                top -= 1
            else:
                flag = 0
        elif i == '-':
            if top > 0:
                num.append((-1) * num.pop(-1) + num.pop(-1))
                top -= 1
            else:
                flag = 0
        elif i == '*':
            if top > 0:
                num.append(num.pop(-1) * num.pop(-1))
                top -= 1
            else:
                flag = 0
        elif i == '/':
            if top > 0:
                num.append((1 / num.pop(-1)) * num.pop(-1))
                top -= 1
            else:
                flag = 0
        elif i == '.':
            break
        else:
            num.append(int(i))
            top += 1
    result = 'error'
    if (top == 0) and flag:
        result = str(int(num.pop(-1)))
    print('#{}'.format(tc + 1), result)
