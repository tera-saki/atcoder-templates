class UnionFind:
    def __init__(self, N):
        self.N = N
        self.par = [-1] * N

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def roots(self):
        return [i for i in range(self.N) if self.par[i] < 0]

    def members(self, x):
        p = self.find(x)
        return [i for i in range(self.N) if self.find(i) == p]


# https://judge.yosupo.jp/problem/unionfind
N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.unite(u, v)
    else:
        print(1 if uf.same(u, v) else 0)
