# 5789_현주의_상자_바꾸기
# 2022-08-09

T = int(input())
n_list = []
q_list = []
all_change = []
for tc in range(T):
    N, Q = map(int, input().split())
    n_list.append(N)
    q_list.append(Q)
    ch_list = []
    for i in range(Q):
        ch_list.append(list(map(int, input().split())))
    all_change.append(ch_list)

for tc in range(T):
    boxes = [0] * n_list[tc]
    for i in range(q_list[tc]):
        for j in range(all_change[tc][i][0] - 1, all_change[tc][i][1]):
            boxes[j] = i + 1

    print('#{}' .format(tc + 1), end='')
    for i in range(n_list[tc]):
        print(' {}' .format(boxes[i]), end='')
    print('')