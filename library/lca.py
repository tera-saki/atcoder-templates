import sys

input = sys.stdin.readline


class LCA:
    def __init__(self, N, E, root=0):
        self.N = N
        self.E = E
        self.K = (N - 1).bit_length()
        self.par = [[-1 for _ in range(N)] for _ in range(self.K)]
        self.depth = [None] * N

        self._dfs(root)
        for k in range(self.K - 1):
            for i in range(self.N):
                if self.par[k][i] < 0:
                    continue
                self.par[k + 1][i] = self.par[k][self.par[k][i]]

    def _dfs(self, root):
        self.depth[root] = 0
        stack = [(root, -1)]
        while stack:
            v, p = stack.pop()
            if not p < 0:
                self.par[0][v] = p
                self.depth[v] = self.depth[p] + 1

            for dest in self.E[v]:
                if dest == p:
                    continue
                stack.append((dest, v))

    def la(self, v, x):
        for k in range(self.K):
            if x & (1 << k):
                v = self.par[k][v]
        return v

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        d = self.depth[v] - self.depth[u]
        v = self.la(v, d)

        if u == v:
            return u
        for k in range(self.K)[::-1]:
            if self.par[k][u] != self.par[k][v]:
                u = self.par[k][u]
                v = self.par[k][v]
        return self.par[0][v]

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]

    def jump(self, u, v, x):
        lca = self.lca(u, v)
        d1 = self.depth[u] - self.depth[lca]
        d2 = self.depth[v] - self.depth[lca]

        if d1 + d2 < x:
            return -1
        if x <= d1:
            return self.la(u, x)
        return self.la(v, d1 + d2 - x)
