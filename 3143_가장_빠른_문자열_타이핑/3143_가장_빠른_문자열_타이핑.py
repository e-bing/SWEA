# 3143_가장_빠른_문자열_타이핑 풀이
# 2022-08-16

T = int(input())
string = []
pattern = []
for tc in range(T):
    a, b = input().split()
    string.append(a)
    pattern.append(b)

for tc in range(T):
    length = 0
    pat_len = 0
    for i in string[tc]:
        length += 1
    result = length
    for i in pattern[tc]:
        pat_len += 1
    i = 0
    while i < (length - pat_len + 1):
        if string[tc][i:i+pat_len] == pattern[tc]:
            result -= pat_len - 1
            i += pat_len
        else:
            i += 1
    print('#{} {}'.format(tc + 1, result))