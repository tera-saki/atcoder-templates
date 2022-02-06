import sys
input = sys.stdin.readline


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
        return self.S[rx + 1][ry + 1] - self.S[lx][ry + 1] - self.S[rx + 1][ly] + self.S[lx][ly]


# https://atcoder.jp/contests/abc106/tasks/abc106_d
N, M, Q = map(int, input().split())
A = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    A[l][r] += 1

S = CumulativeSum2D(A)
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    print(S.sum(p, p, q, q))
