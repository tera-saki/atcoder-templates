from collections import deque


class Dinic:
    def __init__(self, N, inf=1 << 50):
        self.N = N
        self.G = [[] for _ in range(self.N)]
        self.inf = inf

    def add_edge(self, u, v, cap):
        forward = [cap, v, None]
        backward = [0, u, None]
        forward[2] = backward
        backward[2] = forward
        self.G[u].append(forward)
        self.G[v].append(backward)

    def flow(self, s, t):
        flow = 0
        while True:
            self._bfs(s, t)
            if self.level[t] is None:
                return flow
            *self.iter, = map(iter, self.G)
            f = self.inf
            while f > 0:
                f = self._dfs(s, t, self.inf)
                flow += f

    def _bfs(self, s, t):
        self.level = [None] * self.N
        dq = deque([s])
        self.level[s] = 0
        while dq:
            v = dq.popleft()
            for cap, d, _ in self.G[v]:
                if cap == 0:
                    continue
                if self.level[d] is None:
                    self.level[d] = self.level[v] + 1
                    dq.append(d)

    def _dfs(self, u, t, f):
        if u == t:
            return f
        for e in self.iter[u]:
            cap, v, rev = e
            if cap == 0:
                continue
            if self.level[v] > self.level[u]:
                delta = self._dfs(v, t, min(f, cap))
                if delta > 0:
                    e[0] -= delta
                    rev[0] += delta
                    return delta
        return 0
