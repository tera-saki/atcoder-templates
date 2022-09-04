class SegTree:
    def __init__(self, N, func, e):
        self.N = N
        self.func = func
        self.X = [e] * (N << 1)
        self.e = e

    def build(self, seq):
        for i in range(self.N):
            self.X[self.N + i] = seq[i]
        for i in range(self.N)[::-1]:
            self.X[i] = self.func(self.X[i << 1], self.X[i << 1 | 1])

    def add(self, i, x):
        i += self.N
        self.X[i] += x
        while i > 1:
            i >>= 1
            self.X[i] = self.func(self.X[i << 1], self.X[i << 1 | 1])

    def update(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.func(self.X[i << 1], self.X[i << 1 | 1])

    def query(self, L, R):
        L += self.N
        R += self.N
        vL = self.e
        vR = self.e
        while L < R:
            if L & 1:
                vL = self.func(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)
