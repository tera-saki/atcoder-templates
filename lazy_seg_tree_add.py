
import sys
input = sys.stdin.readline

# reference: https://qiita.com/takayg1/items/b7b3f7d458915bcc7a4e


class LazySegTree_RAQ:
    def __init__(self, N, func, e):
        self.N = N
        self.func = func
        self.X = [e] * (N << 1)
        self.lazy = [0] * (N << 1)
        self.e = e

    def build(self, seq):
        for i in range(self.N):
            self.X[self.N + i] = seq[i]
        for i in range(self.N)[::-1]:
            self.X[i] = self.func(self.X[i << 1], self.X[i << 1 | 1])

    def gindex(self, l, r):
        l += self.N
        r += self.N
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in ids[::-1]:
            v = self.lazy[i]
            if not v:
                continue
            self.lazy[i << 1] += v
            self.lazy[i << 1 | 1] += v
            self.X[i << 1] += v
            self.X[i << 1 | 1] += v
            self.lazy[i] = 0

    def add(self, L, R, x):
        *ids, = self.gindex(L, R)
        L += self.N
        R += self.N
        while L < R:
            if L & 1:
                self.lazy[L] += x
                self.X[L] += x
                L += 1
            if R & 1:
                R -= 1
                self.lazy[R] += x
                self.X[R] += x
            L >>= 1
            R >>= 1
        for i in ids:
            self.X[i] = self.func(self.X[i << 1], self.X[i << 1 | 1]) + self.lazy[i]

    def query(self, L, R):
        *ids, = self.gindex(L, R)
        self.propagates(*ids)
        L += self.N
        R += self.N
        vL = self.e
        vR = self.e
        while L < R:
            if L & 1:
                vL = self.func(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.func(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.func(vL, vR)


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
N, Q = map(int, input().split())
lazy_segtree = LazySegTree_RAQ(N, min, 1 << 30)
lazy_segtree.build([0 for _ in range(N)])
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        lazy_segtree.add(s, t + 1, x)
    else:
        s, t = q
        print(lazy_segtree.query(s, t + 1))
