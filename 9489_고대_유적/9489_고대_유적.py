# 9489_고대_유적
# 2022-08-12

T = int(input())
n_list = []
m_list = []
data = []
for tc in range(T):
    N, M = map(int, input().split())
    n_list.append(N)
    m_list.append(M)
    temp = []
    for i in range(N):
        temp.append(list(map(int, input().split())))
    data.append(temp)
for tc in range(T):
    max_cnt = 0
    for i in range(n_list[tc]):
        cnt = 0
        for j in range(m_list[tc]):
            if data[tc][i][j] == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
    for i in range(m_list[tc]):
        cnt = 0
        for j in range(n_list[tc]):
            if data[tc][j][i] == 1:
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                cnt = 0
        if max_cnt < cnt:
            max_cnt = cnt
    print('#{} {}'.format(tc + 1, max_cnt))