import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


class LCA:
    def __init__(self, N, E, root=0):
        self.N = N
        self.E = E
        self.K = N.bit_length()
        self.par = [[-1 for _ in range(N)] for _ in range(self.K)]
        self.depth = [None] * N

        self.dfs(root, 0, -1)
        for k in range(self.K - 1):
            for i in range(self.N):
                if self.par[k][i] < 0:
                    continue
                self.par[k + 1][i] = self.par[k][self.par[k][i]]

    def dfs(self, v, d, p):
        self.par[0][v] = p
        self.depth[v] = d
        for dest in self.E[v]:
            if dest == p:
                continue
            self.dfs(dest, d + 1, v)

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        d = self.depth[v] - self.depth[u]
        for k in range(self.K):
            if d & (1 << k):
                v = self.par[k][v]

        if u == v:
            return u
        for k in range(self.K)[::-1]:
            if self.par[k][u] != self.par[k][v]:
                u = self.par[k][u]
                v = self.par[k][v]
        return self.par[0][v]

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]