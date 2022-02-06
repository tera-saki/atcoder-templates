import sys
input = sys.stdin.readline


class LIS:
    def __init__(self, N, A):
        self.N = N
        self.A = A

    def solve(self):
        L = [self.A[0]]
        for i in range(1, self.N):
            if self.A[i] > L[-1]:
                L.append(self.A[i])
            else:
                l = -1
                r = len(L)
                while r - l > 1:
                    c = (l + r) // 2
                    if L[c] >= self.A[i]:
                        r = c
                    else:
                        l = c
                L[r] = self.A[i]
        return len(L)


N = int(input())
A = [int(input()) for _ in range(N)]
print(LIS(N, A).solve())
