# 1224_계산기3 풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    data_len = int(input())
    data = input()
    operators = {'*': [2, 2], '+': [1, 1], '(': [0, 3]}
    stack = []
    top = -1
    result = ''
    for token in data:
        if token == ')':
            while stack[top] != '(':
                result += stack.pop(-1)
                top -= 1
            stack.pop(-1)
            top -= 1
        elif token in operators.keys():
            if top < 0:
                stack.append(token)
                top += 1
            else:
                while (top >= 0) and (operators[token][1] <= operators[stack[top]][0]):
                    result += stack.pop(-1)
                    top -= 1
                stack.append(token)
                top += 1
        else:
            result += token
    while top >= 0:
        result += stack.pop(-1)
        top -= 1

    num_stack = []
    num_top = -1
    for token in result:
        if token == '+':
            num_stack.append(num_stack.pop() + num_stack.pop())
            num_top -= 1
        elif token == '*':
            num_stack.append(num_stack.pop() * num_stack.pop())
            num_top -= 1
        else:
            num_stack.append(int(token))
            num_top += 1
    print('#{} {}'.format(tc + 1, num_stack.pop()))
