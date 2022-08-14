# 연습문제3_고지식한_패턴_검색
# 2022-08-12

T = int(input())
pattern = []
my_str = []
for tc in range(T):
    pattern.append(input())
    my_str.append(input())
for tc in range(T):
    pat_len = 0
    str_len = 0
    flag = 0
    for i in pattern[tc]:
        pat_len += 1
    for i in my_str[tc]:
        str_len += 1
    for i in range(str_len - pat_len + 1):
        for j in range(pat_len):
            if my_str[tc][i + j] != pattern[tc][j]:
                break
            elif j == pat_len - 1:
                flag = 1
        if flag:
            break
    print('#{}'.format(tc + 1), flag)
