from typing import List, Tuple, Optional


class BellmanFord:
    def __init__(self, N: int, E: List[List[Tuple[int, int]]],
                 start: int = 0, inf: int = 1 << 60):
        self.N = N
        self.E = E
        self.start = start
        self.inf = inf
        self.C = [self.inf] * N

        self._calculate()

    def get_cost(self, i: int) -> int:
        """
        return the cost to i-th vertex from start.
        If the return value is inf, the vertex is unreachable.
        If the return value is -inf, the path to the vertex includes negative cycle.
        """
        return self.C[i]

    def _calculate(self):
        self.C[self.start] = 0
        for _ in range(self.N - 1):
            update = False
            for u in range(self.N):
                if self.C[u] == self.inf:
                    continue
                for c, v in self.E[u]:
                    if self.C[v] > self.C[u] + c:
                        self.C[v] = self.C[u] + c
                        update = True
            if not update:
                break

        nc = [False] * self.N
        for _ in range(self.N):
            for u in range(self.N):
                if self.C[u] == self.inf:
                    continue
                for c, v in self.E[u]:
                    if self.C[v] > self.C[u] + c:
                        self.C[v] = self.C[u] + c
                        nc[v] = True
                    if nc[u]:
                        nc[v] = True

        for u in range(self.N):
            if nc[u]:
                self.C[u] = -self.inf
