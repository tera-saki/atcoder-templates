import sys
from typing import List, Optional
from collections import deque


class TopologicalSort():
    def __init__(self, N: int, E: List[List[int]]) -> None:
        self.N = N
        self.E = E
        self.D = [0] * N
        for s in range(self.N):
            for t in self.E[s]:
                self.D[t] += 1

    def sort(self) -> Optional[List[int]]:
        """return sorted list if sortable otherwise None"""
        dq = deque([])
        for i in range(self.N):
            if self.D[i] == 0:
                dq.append(i)

        ret = []
        while dq:
            v = dq.popleft()
            ret.append(v)
            for dest in self.E[v]:
                self.D[dest] -= 1
                if self.D[dest] == 0:
                    dq.append(dest)

        for i in range(self.N):
            if not self.D[i] == 0:
                return None
        return ret
