# 1232_사칙연산 풀이
# 2022-09-15

import sys
sys.stdin = open('input.txt', 'r')


def operate(operator):
    my_operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    b = stack.pop(-1)
    a = stack.pop(-1)
    stack.append(my_operators[operator](a, b))


def order(n):
    try:
        order(ch1[n])
        order(ch2[n])
        operate(nodes[n])
    except KeyError:
        stack.append(nodes[n])


for tc in range(10):
    operators = ['+', '-', '/', '*']
    ch1 = {}
    ch2 = {}
    nodes = {}
    stack = []
    N = int(input())
    for i in range(N):
        data = input().split()
        if data[1] in operators:
            nodes[int(data[0])] = data[1]
            ch1[int(data[0])] = int(data[2])
            ch2[int(data[0])] = int(data[3])
        else:
            nodes[int(data[0])] = int(data[1])
    order(1)
    result = stack.pop()
    print('#{} {}'.format(tc + 1, result))
