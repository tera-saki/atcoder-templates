# https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/GRL_4_B/judge/6940421/Python3
import sys
from typing import List, Optional
from collections import deque
input = sys.stdin.readline


class TopologicalSort():
    def __init__(self, N: int, E: List[List[int]]) -> None:
        self.N = N
        self.E = E
        self.D = [0] * N
        for s in range(self.N):
            for t in self.E[s]:
                self.D[t] += 1

    def sort(self) -> Optional[List[int]]:
        """return sorted list if sortable othereise None"""
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


N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)

ret = TopologicalSort(N, E).sort()
print(*ret, sep='\n')
