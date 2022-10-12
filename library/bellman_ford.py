class BellmanFord:
    def __init__(self, N, E, start=0, inf=1 << 50):
        self.N = N
        self.E = E
        self.start = start
        self.inf = inf
        self.C = [self.inf] * N

        self.negative_cycle = False
        self._calculate()

    def get_cost(self, i):
        return self.C[i] if not self.negative_cycle else None

    def _calculate(self):
        self.C[self.start] = 0
        for cnt in range(self.N):
            update = False
            for u in range(self.N):
                if self.C[u] == self.inf:
                    continue
                for c, v in self.E[u]:
                    if self.C[v] > self.C[u] + c:
                        self.C[v] = self.C[u] + c
                        update = True
            if not update:
                return
        self.negative_cycle = True
