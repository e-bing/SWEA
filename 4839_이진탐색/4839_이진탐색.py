# 4839_이진탐색 풀이
# 2022-08-11

def binary_search(start, end, goal):
    mid = (start + end) // 2
    count = 0
    while mid != goal:
        if goal > mid:
            start = mid
        else:
            end = mid
        mid = (start + end) // 2
        count += 1
    return count


T = int(input())
P = []
page_a = []
page_b = []
for tc in range(T):
    temp_P, temp_a, temp_b = map(int, input().split())
    P.append(temp_P)
    page_a.append(temp_a)
    page_b.append(temp_b)

for tc in range(T):
    count_a = binary_search(1, P[tc], page_a[tc])
    count_b = binary_search(1, P[tc], page_b[tc])
    if count_a > count_b:
        result = 'B'
    elif count_a == count_b:
        result = '0'
    else:
        result = 'A'
    print('#{}'.format(tc + 1), result)
