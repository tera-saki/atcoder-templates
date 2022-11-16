from typing import List, Tuple, Optional
from collections import deque


class BFS:
    def __init__(self, N: int, E: List[List[int]],
                 start: int = 0, inf: int = 1 << 50):
        self.N = N
        self.E = E
        self.start = start
        self.inf = inf

        self.C = [self.inf] * N
        self.prev = [None] * N

        self._search()

    def get_cost(self, i: int) -> int:
        return self.C[i]

    def get_path(self, i: int) -> Optional[List[int]]:
        if not self.reachable(i):
            return None

        p = []
        cur = i
        while cur is not None:
            p.append(cur)
            cur = self.prev[cur]
        p.reverse()
        return p

    def reachable(self, i: int) -> bool:
        return self.C[i] < self.inf

    def _search(self) -> None:
        dq = deque([(self.start, -1)])
        self.C[self.start] = 0
        while dq:
            v, p = dq.popleft()
            if p >= 0:
                self.prev[v] = p
            for d in self.E[v]:
                if self.C[d] > self.C[v] + 1:
                    self.C[d] = self.C[v] + 1
                    dq.append((d, v))
