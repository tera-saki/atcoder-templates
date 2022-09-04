import sys


class PrimeTable:
    def __init__(self, N):
        self.is_prime = [True] * (N + 1)

        self.is_prime[0] = False
        self.is_prime[1] = False
        for i in range(2, N + 1):
            if i * i > N:
                break
            if self.is_prime[i] is False:
                continue
            for j in range(2, N + 1):
                if i * j > N:
                    break
                self.is_prime[i * j] = False

        self.primes = [n for n in range(2, N + 1) if self.is_prime[n]]

    def is_prime(self, n):
        return self.is_prime[n]


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009
primes = PrimeTable(10 ** 6).primes
for n in map(int, sys.stdin.read().split()):
    l = -1
    r = len(primes)
    while r - l > 1:
        c = (l + r) // 2
        if primes[c] == n:
            l = c
            break
        if primes[c] < n:
            l = c
        else:
            r = c
    print(l + 1)
