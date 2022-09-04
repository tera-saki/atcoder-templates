from collections import deque
import sys
input = sys.stdin.readline


class TopologicalSort():
    def __init__(self, N, E):
        self.N = N
        self.E = E
        self.D = [0] * N
        for s in range(N):
            for t in E[s]:
                self.D[t] += 1

    def sort(self):
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
                return False, None
        return True, ret
