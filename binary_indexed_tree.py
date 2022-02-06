class BIT:
    def __init__(self, N):
        self.N = N
        self.X = [0] * (N + 1)

    def add(self, i, x):
        while i <= self.N:
            self.X[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.X[i]
            i -= i & -i
        return s

    def max(self, i):
        s = -float('inf')
        while i > 0:
            s = max(s, self.X[i])
            i -= i & -i
        return s

    def lower_bound(self, x):
        s = 0
        cur = 0
        for i in range(self.N.bit_length(), -1, -1):
            k = cur + (1 << i)
            if k <= self.N and s + self.X[k] < x:
                s += self.X[k]
                cur += 1 << i
        return cur + 1, s

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
N = int(input())
A = list(map(int, input().split()))
idx = {}
for i, a in enumerate(sorted(A)):
    idx[a] = i + 1

bit = BIT(N)
ans = 0
for i in range(N):
    ans += i - bit.sum(idx[A[i]])
    bit.add(idx[A[i]], 1)
print(ans)