# 1219_길찾기 풀이
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


for tc in range(10):
    case, link = map(int, input().split())
    data = list(map(int, input().split()))
    road_1 = [-1] * 100
    road_2 = [-1] * 100
    for i in range(link):
        if road_1[data[2 * i]] == -1:
            road_1[data[2 * i]] = data[2 * i + 1]
        else:
            road_2[data[2 * i]] = data[2 * i + 1]
    my_stack = Stack()
    my_stack.push(0)
    cur = 0
    result = 0
    visited = [False] * 100
    while my_stack.top >= 0:
        if (road_1[cur] != -1) and (visited[road_1[cur]] is False):
            if road_2[cur] != -1:
                my_stack.push(cur)
            cur = road_1[cur]
            visited[cur] = True
        elif (road_2[cur] != -1) and (visited[road_2[cur]] is False):
            cur = road_2[cur]
            visited[cur] = True
        else:
            if my_stack.top >= 0:
                cur = my_stack.pop()
        if cur == 99:
            result = 1
            break
    print('#{} {}'.format(tc + 1, result))
