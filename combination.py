class Combination:
    def __init__(self, N, p):
        self.N = N
        self.p = p
        self.f = [None] * (N + 1)
        self.finv = [None] * (N + 1)
        self.inv = [None] * (N + 1)

        self.f[0] = 1
        self.f[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, N + 1):
            self.f[i] = self.f[i - 1] * i % p
            self.inv[i] = p - self.inv[p % i] * (p // i) % p
            self.finv[i] = self.finv[i - 1] * self.inv[i] % p

    def P(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.f[n] * self.finv[n - k] % self.p

    def C(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.f[n] * (self.finv[k] * self.finv[n - k] % self.p) % self.p

    # 重複組合せ
    # n種類のものからk個選ぶ
    def H(self, n, k):
        return self.C(k + n - 1, k)
