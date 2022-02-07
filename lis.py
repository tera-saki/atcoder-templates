import sys
input = sys.stdin.readline


class LIS:
    def __init__(self, N, A):
        self.N = N
        self.A = A

    def solve(self):
        S = [self.A[0]]
        for i in range(1, self.N):
            if self.A[i] > S[-1]:
                S.append(self.A[i])
            else:
                l = -1
                r = len(S)
                while r - l > 1:
                    c = (l + r) // 2
                    if S[c] >= self.A[i]:
                        r = c
                    else:
                        l = c
                S[r] = self.A[i]
        return len(S)


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=ja
N = int(input())
A = [int(input()) for _ in range(N)]
print(LIS(N, A).solve())
