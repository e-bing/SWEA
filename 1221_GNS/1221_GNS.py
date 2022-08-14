# 1221_GNS 풀이
# 2022-08-12

T = int(input())
testcase = []
length = []
num_list = []
data = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(T):
    temp_case, temp_len = input().split()
    testcase.append(temp_case)
    length.append(int(temp_len))
    num_list.append(list(input().split()))

for tc in range(T):
    for i in range(length[tc]):
        for j in range(10):
            if num_list[tc][i] == data[j]:
                num_list[tc][i] = j
                break
    num_list[tc] = sorted(num_list[tc])
    for i in range(length[tc]):
        for j in range(10):
            if num_list[tc][i] == j:
                num_list[tc][i] = data[j]
                break
    print(testcase[tc])
    print(*num_list[tc])
