# 1945_간단한_소인수분해
# 2022-08-09

T = int(input())
n_list = []
for tc in range(T):
    n_list.append(int(input()))
for tc in range(T):
    primes = [2, 3, 5, 7, 11]
    shares = [0, 0, 0, 0, 0]
    for i in range(5):
        while n_list[tc] % primes[i] == 0:
            n_list[tc] /= primes[i]
            shares[i] += 1

    print('#{}' .format(tc+1), end='')
    for i in range(5):
        print(' {}' .format(shares[i]), end='')
    print()