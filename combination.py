import sys
input = sys.stdin.readline


class Combination:
    def __init__(self, N, mod):
        self.N = N
        self.mod = mod
        self.f = [None] * (N + 1)
        self.finv = [None] * (N + 1)
        self.inv = [None] * (N + 1)

        self.f[0] = 1
        self.f[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, N + 1):
            self.f[i] = self.f[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def P(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.f[n] * self.finv[n - k] % self.mod

    def C(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.f[n] * (self.finv[k] * self.finv[n - k] % self.mod) % self.mod

    # 重複組合せ
    # n種類のものからk個選ぶ
    def H(self, n, k):
        if n == 0 and k == 0:
            return 1
        return self.C(k + n - 1, k)


# https://yukicoder.me/problems/no/117
T = int(input())
mod = 10 ** 9 + 7
comb = Combination(2 * 10 ** 6, mod)

for _ in range(T):
    query = input()[:-1]
    t = query[0]
    n, k = map(int, query[2:-1].split(','))
    if t == 'C':
        print(comb.C(n, k))
    elif t == 'P':
        print(comb.P(n, k))
    else:
        print(comb.H(n, k))
