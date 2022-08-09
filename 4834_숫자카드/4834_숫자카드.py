# 4834_숫자카드 풀이
# 2022-08-09

def counting(data):
    max_num = data[0]
    for i in data:
        if max_num < i:
            max_num = i

    counts = [0] * (max_num + 1)
    for i in data:
        counts[i] += 1

    return counts

def return_max(data, counts, max_counts):
    flag = 0
    duplication = 0
    idx = -1
    max_idx = -1
    max_list = []

    for i in counts:
        idx += 1
        if flag == 0 and i == max_counts:
            flag = 1
            max_idx = idx
            max_list.append(idx)
        elif i == max_counts:
            duplication = 1
            max_list.append(idx)
    if duplication == 1:
        return max_list[-1]
    else:
        return max_idx

T = int(input())
card_num = []
card_list = []
for tc in range(T):
    card_num.append(int(input()))
    card_list.append(list(map(int, input())))

for tc in range(T):
    counts = counting(card_list[tc])

    max_counts = 0
    for i in counts:
        if max_counts < i:
            max_counts = i

    max = return_max(card_list[tc], counts, max_counts)
    print('#{} {} {}' .format(tc+1, max, max_counts))