from typing import List, Tuple, Optional
import heapq


class Dijkstra:
    def __init__(self, N: int, E: List[List[Tuple[int, int]]],
                 start: int = 0, inf: int = 1 << 50):
        self.N = N
        self.E = E
        self.start = start
        self.inf = inf

        self.C = [self.inf] * N
        self.prev = [None] * N
        self._calculate()

    def get_cost(self, i: int) -> Optional[int]:
        """return cost to i-th vertex. return inf if the vertex is unreachable."""
        return self.C[i]

    def get_path(self, i) -> Optional[List[int]]:
        """return shortest path to i-th vertex if reachable otherwise None"""
        if not self.reachable(i):
            return None

        p = []
        cur = i
        while cur is not None:
            p.append(cur)
            cur = self.prev[cur]
        p.reverse()
        return p

    def reachable(self, i) -> bool:
        """return whether i-th vertex is reachable from start"""
        return self.C[i] < self.inf

    def _calculate(self) -> None:
        h = [(0, self.start)]
        self.C[self.start] = 0
        visited = [False] * self.N

        while h:
            _, v = heapq.heappop(h)
            if visited[v] is True:
                continue
            visited[v] = True

            for c, d in self.E[v]:
                if self.C[d] > self.C[v] + c:
                    self.C[d] = self.C[v] + c
                    self.prev[d] = v
                    heapq.heappush(h, (self.C[d], d))
