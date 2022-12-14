class Lowlink:
    # cf: https://codeforces.com/blog/entry/68138
    def __init__(self, N, E):
        self.N = N
        self.E = E
        # span-edge and back-edge (directed)
        self.span = [[] for _ in range(self.N)]
        self.back = [[] for _ in range(self.N)]

        self.ord = [None] * self.N
        self.low = [None] * self.N
        self.par = [None] * self.N

        self._build()

    def _build(self):
        visited = [False] * self.N
        cnt = 0
        for i in range(self.N):
            if visited[i]:
                continue
            stack = [(i, -1)]
            while stack:
                v, p = stack.pop()

                if v < 0:
                    v = ~v
                    for d in self.span[v]:
                        if d == p:
                            continue
                        self.low[v] = min(self.low[v], self.low[d])
                    continue

                if visited[v]:
                    continue
                visited[v] = True
                self.ord[v] = cnt
                self.low[v] = cnt
                cnt += 1
                # p -> v is span-edge.
                self.par[v] = p
                if p >= 0:
                    self.span[p].append(v)
                stack.append((~v, p))

                for d in self.E[v][::-1]:
                    if d == p:
                        continue
                    if visited[d]:
                        # v -> d is back-edge since v is already visited.
                        self.back[v].append(d)
                        self.low[v] = min(self.low[v], self.ord[d])
                        continue
                    stack.append((d, v))

    def bridges(self):
        """return list of edges that are bridges"""
        bridges = []
        for u in range(self.N):
            for v in self.span[u]:
                # vertex u has child v that does not have lowlink to pass over its parent
                if self.ord[u] < self.low[v]:
                    bridges.append((u, v))
        return bridges

    def articulation_points(self):
        """return list of vertices that are articulation points"""
        points = []
        for u in range(self.N):
            if self.par[u] < 0:
                if len(self.span[u]) >= 2:
                    points.append(u)
                continue
            for v in self.span[u]:
                if self.ord[u] <= self.low[v]:
                    points.append(u)
                    break
        return points
