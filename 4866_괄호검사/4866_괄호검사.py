# 4866_괄호검사 풀이
# 2022-08-18

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.stack.pop(-1)
        else:
            return -1


T = int(input())
parentheses = {'>': '<', ')': '(', ']': '[', '}': '{'}
for tc in range(T):
    data = input()
    my_stack = Stack()
    result = 1
    for i in data:
        if i in parentheses.values():
            my_stack.push(i)
        elif i in parentheses.keys():
            if my_stack.pop() != parentheses[i]:
                result = 0
                break
    if my_stack.top >= 0:
        result = 0
    print('#{} {}'.format(tc + 1, result))