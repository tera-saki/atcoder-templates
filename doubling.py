import sys
input = sys.stdin.readline


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


# https://atcoder.jp/contests/abc167/tasks/abc167_d
N, K = map(int, input().split())
nex = list(map(lambda x: int(x) - 1, input().split()))
solver = Doubling(nex)
print(solver.solve(0, K) + 1)
