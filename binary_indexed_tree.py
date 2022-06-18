import sys
input = sys.stdin.readline


class BIT:
    # 0-indexed
    def __init__(self, N):
        self.N = N
        self.X = [0] * (N + 1)

    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.X[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.X[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l)

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


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
N, Q = map(int, input().split())
bit = BIT(N)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        s -= 1
        bit.add(s, x)
        bit.add(t, -x)
    else:
        t, = q
        print(bit.range_sum(0, t))
