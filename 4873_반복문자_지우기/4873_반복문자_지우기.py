# 4873_반복문자_지우기 풀이
# 2022-08-18

class Stack:
    def __init__(self, size):
        self.stack = []
        self.top = 0
        self.size = size

    def push(self, item):
        if self.top + 1 == self.size:
            print('overflow!')
        else:
            self.top += 1
            self.stack.append(item)

    def pop(self):
        if self.top <= 0:
            print('underflow!')
            return 0
        else:
            self.top -= 1
            return self.stack.pop(-1)


T = int(input())
for tc in range(T):
    data = list(input())
    length = 0
    idx = 0
    for i in data:
        length += 1
    my_stack = Stack(length)
    for i in data:
        if (my_stack.top > 0) and my_stack.stack[my_stack.top - 1] == i:
            my_stack.pop()
        else:
            my_stack.push(i)
    print('#{} {}'.format(tc + 1, my_stack.top))