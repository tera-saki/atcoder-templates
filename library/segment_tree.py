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

    def get(self, i):
        i += self.N
        return self.X[i]

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

    def query(self, l, r):
        l += self.N
        r += self.N
        vl = self.e
        vr = self.e
        while l < r:
            if l & 1:
                vl = self.func(vl, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                vr = self.func(self.X[r], vr)
            l >>= 1
            r >>= 1
        return self.func(vl, vr)
