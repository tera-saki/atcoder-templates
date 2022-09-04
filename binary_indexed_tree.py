class BIT:
    def __init__(self, N):
        self.N = N
        self.A = [0] * (N + 1)

    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.A[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l)
