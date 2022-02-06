class Matpow:
    def __init__(self, N, A, p):
        self.N = N
        self.A = A
        self.p = p
        self.digit = 60
        self.doubling = [None] * self.digit

        self.doubling[0] = A
        for i in range(1, self.digit):
            self.doubling[i] = self.mul(self.doubling[i - 1], self.doubling[i - 1])

    def pow(self, n):
        E = [[1 if i == j else 0 for j in range(self.N)] for i in range(self.N)]
        acc = E
        for k in range(self.digit):
            if n & (1 << k):
                acc = self.mul(acc, self.doubling[k])
        return acc

    def mul(self, A, B):
        C = [[0 for _ in range(self.N)] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                for k in range(self.N):
                    C[i][j] += A[i][k] * B[k][j]
                    C[i][j] %= self.p
        return C
