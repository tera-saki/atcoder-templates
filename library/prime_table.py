# https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/0053/judge/6971267/Python3
import sys
input = sys.stdin.readline


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


primes = PrimeTable(10 ** 6).primes
S = [0]
for p in primes:
    S.append(S[-1] + p)
while True:
    n = int(input())
    if n == 0:
        break
    print(S[n])
