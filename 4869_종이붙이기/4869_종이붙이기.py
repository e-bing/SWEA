# 4869_종이붙이기 풀이
# 2022-08-18

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, item):
        self.top += 1
        self.stack.append(item)

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            return self.stack.pop(-1)
        else:
            return -1


T = int(input())
for tc in range(T):
    data = int(input()) // 10
    result = Stack()
    result.push(1)
    result.push(3)
    for i in range(2, data):
        result.push(result.stack[i - 2] * 2 + result.stack[i - 1])
    print('#{} {}'.format(tc + 1, result.pop()))
