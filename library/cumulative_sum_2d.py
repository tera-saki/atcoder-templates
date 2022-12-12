class CumulativeSum2D:
    def __init__(self, A):
        self.A = A
        self.H = len(A)
        self.W = len(A[0])
        self.S = [0] * ((self.W + 1) * (self.H + 1))

        for i in range(self.H):
            for j in range(self.W):
                self.S[self.id(i + 1, j + 1)] = self.S[self.id(i + 1, j)] + self.S[(self.id(i, j + 1))] - self.S[(self.id(i, j))] + self.A[i][j]

    def sum(self, lx, ly, rx, ry):
        """return sum of area s.t. lx <= x < rx and ly <= y < ry (0-indexed)"""
        return self.S[self.id(rx, ry)] - self.S[self.id(lx, ry)] - self.S[self.id(rx, ly)] + self.S[self.id(lx, ly)]

    def id(self, x, y):
        return x * self.W + y
