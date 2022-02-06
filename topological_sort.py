from collections import deque
import sys
input = sys.stdin.readline


class TopologicalSort():
    def __init__(self, N, E, D):
        self.N = N
        self.E = E
        self.D = D

    def sort(self):
        dq = deque([])
        for i in range(self.N):
            if self.D[i] == 0:
                dq.append(i)
        if len(dq) == 0:
            return False, None

        ret = []
        while len(dq) > 0:
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


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B
N, M = map(int, input().split())
E = [[] for _ in range(N)]
D = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    D[b] += 1

_, ret = TopologicalSort(N, E, D).sort()
print(*ret, sep='\n')
