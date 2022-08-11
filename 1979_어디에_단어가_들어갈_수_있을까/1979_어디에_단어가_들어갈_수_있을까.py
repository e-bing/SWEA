# 1979_어디에_단어가_들어갈_수_있을까 풀이
# 2022-08-11

T = int(input())
n_list = []
k_list = []
puzzle = []
for tc in range(T):
    N, K = map(int, input().split())
    n_list.append(N)
    k_list.append(K)
    puzzle.append([])
    for i in range(N):
        puzzle[tc].append(list(map(int, input().split())))

for tc in range(T):
    result = 0
    for i in range(n_list[tc]):
        count_x = 0
        count_y = 0
        for j in range(n_list[tc]):
            if puzzle[tc][j][i] == 1:
                count_x += 1
            else:
                if count_x == k_list[tc]:
                    result += 1
                count_x = 0
            if puzzle[tc][i][j] == 1:
                count_y += 1
            else:
                if count_y == k_list[tc]:
                    result += 1
                count_y = 0
        if count_x == k_list[tc]:
            result += 1
        if count_y == k_list[tc]:
            result += 1
    print('#{} {}' .format(tc + 1, result))
