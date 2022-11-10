class Doubling:
    def __init__(self, nex, digit=60):
        self.d = [[None for _ in range(len(nex))] for _ in range(digit)]
        self.digit = digit

        self.d[0] = nex
        for i in range(1, self.digit):
            for j in range(len(nex)):
                self.d[i][j] = self.d[i - 1][self.d[i - 1][j]]

    def solve(self, start, k):
        p = start
        for i in range(self.digit):
            if k & 1:
                p = self.d[i][p]
            k >>= 1
        return p


class DoublingMonoid:
    def __init__(self, nex, A, op, e, digit=60):
        self.op = op
        self.e = e
        self.digit = digit

        self.L = len(nex)
        self.d = [[None for _ in range(self.L)] for _ in range(digit)]
        self.S = [[e for _ in range(self.L)] for _ in range(digit)]

        self.d[0] = nex
        self.S[0] = A
        for i in range(1, self.digit):
            for j in range(self.L):
                self.d[i][j] = self.d[i - 1][self.d[i - 1][j]]
                self.S[i][j] = self.op(self.S[i - 1][j], self.S[i - 1][self.d[i - 1][j]])

    def solve(self, start, k):
        p = start
        acc = self.e
        for i in range(self.digit):
            if k & 1:
                acc = self.op(acc, self.S[i][p])
                p = self.d[i][p]
            k >>= 1
        return acc
