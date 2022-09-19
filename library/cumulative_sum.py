class CumulativeSum2D:
    def __init__(self, A):
        self.A = A
        self.H = len(A)
        self.W = len(A[0])
        self.S = [[0 for _ in range(self.W + 1)] for _ in range(self.H + 1)]

        for i in range(self.H):
            for j in range(self.W):
                self.S[i + 1][j + 1] = self.S[i + 1][j] + self.S[i][j + 1] - self.S[i][j] + self.A[i][j]

    def sum(self, lx, ly, rx, ry):
        """return sum of area s.t. lx <= x <= rx and ly <= y <= ry (0-indexed)"""
        return self.S[rx + 1][ry + 1] - self.S[lx][ry + 1] - self.S[rx + 1][ly] + self.S[lx][ly]
