class TreeDiameter:
    def __init__(self, N, E, inf=1 << 50):
        self.N = N
        self.E = E
        self.inf = inf

        self.prev = [None] * N

        u, c0 = self._dfs1(0)
        v, cu = self._dfs2(u)
        self.diameter = (u, v)
        self.diameter_weight = cu[v]

    def get_path(self):
        _, v = self.diameter
        cur = v
        p = []
        while cur is not None:
            p.append(cur)
            cur = self.prev[cur]
        return p

    def _dfs1(self, s):
        cost = [self.inf] * self.N
        cost[s] = 0
        stack = [s]
        farthest = s
        while stack:
            v = stack.pop()
            if cost[v] > cost[farthest]:
                farthest = v
            for c, d in self.E[v]:
                if cost[d] > cost[v] + c:
                    cost[d] = cost[v] + c
                    stack.append(d)
        return farthest, cost

    def _dfs2(self, s):
        cost = [self.inf] * self.N
        cost[s] = 0
        stack = [(s, -1)]
        farthest = s
        while stack:
            v, p = stack.pop()
            if not p < 0:
                self.prev[v] = p
            if cost[v] > cost[farthest]:
                farthest = v
            for c, d in self.E[v]:
                if cost[d] > cost[v] + c:
                    cost[d] = cost[v] + c
                    stack.append((d, v))
        return farthest, cost
