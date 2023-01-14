class BIT:
    def __init__(self, N):
        self.N = N
        self.A = [0] * (N + 1)

    def build(self, A):
        """build BIT with given list"""
        for i, a in enumerate(A):
            self.A[i + 1] = a
        for i in range(1, self.N):
            if i + (i & -i) > self.N:
                continue
            self.A[i + (i & -i)] += self.A[i]

    def add(self, i, x):
        """add x to i-th element (0-indexed)"""
        assert 0 <= i < self.N
        i += 1
        while i <= self.N:
            self.A[i] += x
            i += i & -i

    def sum(self, i):
        """return sum(A[:i])"""
        assert 0 <= i <= self.N
        s = 0
        while i > 0:
            s += self.A[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        """return sum(A[l:r])"""
        return self.sum(r) - self.sum(l)
