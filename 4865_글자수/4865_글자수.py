# 4865_글자수 풀이
# 2022-08-16

T = int(input())
pattern = []
string = []
for tc in range(T):
    pattern.append(input())
    string.append(input())

for tc in range(T):
    str_dict = {}
    result = 0
    for i in string[tc]:
        if i in str_dict.keys():
            str_dict[i] += 1
        else:
            str_dict[i] = 1
    for i in pattern[tc]:
        if (i in str_dict) and (result < str_dict[i]):
            result = str_dict[i]
    print('#{} {}'.format(tc + 1, result))
