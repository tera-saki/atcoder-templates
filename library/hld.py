from typing import List, Tuple


class HLD:
    # reference: https://codeforces.com/blog/entry/53170
    def __init__(self, N, E, root: int = 0):
        self.N = N
        self.E = E
        self.root = root

        self.D = [0] * self.N
        self.par = [-1] * self.N
        self.sz = [0] * self.N
        self.top = [0] * self.N

        self.ord = [None] * self.N

        self._dfs_sz()
        self._dfs_hld()

    def path_query_range(self, u: int, v: int, is_edge_query: bool = False) -> List[Tuple[int, int]]:
        """return list of [l, r) ranges that cover u-v path"""
        ret = []
        while True:
            if self.ord[u] > self.ord[v]:
                u, v = v, u
            if self.top[u] == self.top[v]:
                ret.append((self.ord[u] + is_edge_query, self.ord[v] + 1))
                return ret
            ret.append((self.ord[self.top[v]], self.ord[v] + 1))
            v = self.par[self.top[v]]

    def subtree_query_range(self, v: int, is_edge_query: bool = False) -> Tuple[int, int]:
        """return [l, r) range that cover vertices of subtree v"""
        return (self.ord[v] + is_edge_query, self.ord[v] + self.sz[v])

    def get_index(self, v: int) -> int:
        """return euler tour order of given vertex"""
        return self.ord[v]

    def lca(self, u, v):
        while True:
            if self.ord[u] > self.ord[v]:
                u, v = v, u
            if self.top[u] == self.top[v]:
                return u
            v = self.par[self.top[v]]

    def dist(self, u, v):
        return self.D[u] + self.D[v] - 2 * self.D[self.lca(u, v)]

    def _dfs_sz(self):
        stack = [(self.root, -1)]
        while stack:
            v, p = stack.pop()
            if v < 0:
                v = ~v
                self.sz[v] = 1
                for i, dst in enumerate(self.E[v]):
                    if dst == p:
                        continue
                    self.sz[v] += self.sz[dst]
                    # v -> E[v][0] will be heavy path
                    if self.sz[self.E[v][0]] < self.sz[dst]:
                        self.E[v][0], self.E[v][i] = self.E[v][i], self.E[v][0]
            else:
                if ~p:
                    self.D[v] = self.D[p] + 1
                    self.par[v] = p
                # avoid first element of E[v] is parent of vertex v if v has some children
                if len(self.E[v]) >= 2 and self.E[v][0] == p:
                    self.E[v][0], self.E[v][1] = self.E[v][1], self.E[v][0]
                stack.append((~v, p))
                for dst in self.E[v]:
                    if dst == p:
                        continue
                    stack.append((dst, v))

    def _dfs_hld(self):
        stack = [(self.root, -1)]
        cnt = 0
        while stack:
            v, p = stack.pop()
            self.ord[v] = cnt
            cnt += 1
            heavy_path_idx = len(self.E[v]) - 1
            for i, dst in enumerate(self.E[v][::-1]):
                if dst == p:
                    continue
                # top[dst] is top[v] if v -> dst is heavy path otherwise dst itself
                self.top[dst] = self.top[v] if i == heavy_path_idx else dst
                stack.append((dst, v))
