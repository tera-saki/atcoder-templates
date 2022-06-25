import sys
from operator import lt, le
input = sys.stdin.readline


class LIS:
    def __init__(self, N, A):
        self.N = N
        self.A = A

    def solve(self, strict=True):
        S = [self.A[0]]
        cmp = lt if strict else le
        for i in range(1, self.N):
            if cmp(S[-1], self.A[i]):
                S.append(self.A[i])
            else:
                l = -1
                r = len(S)
                while r - l > 1:
                    c = (l + r) // 2
                    if cmp(S[c], self.A[i]):
                        l = c
                    else:
                        r = c
                S[r] = self.A[i]
        return len(S)


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=ja
N = int(input())
A = [int(input()) for _ in range(N)]
print(LIS(N, A).solve())
