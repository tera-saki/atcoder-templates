import heapq
import sys
input = sys.stdin.readline


class Dijkstra:
    def __init__(self, N, E, inf=1 << 40):
        self.N = N
        self.E = E
        self.inf = inf

    def cost_from(self, s):
        C = [self.inf] * self.N
        C[s] = 0
        h = [(0, s)]
        visited = set()

        while len(h) > 0:
            _, v = heapq.heappop(h)
            if v in visited:
                continue
            visited.add(v)

            for c, dest in self.E[v]:
                if C[dest] > C[v] + c:
                    C[dest] = C[v] + c
                    heapq.heappush(h, (C[dest], dest))
        return C


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
N, M, s = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E[a].append((c, b))

D = Dijkstra(N, E)
C = D.cost_from(s)
for i in range(N):
    print(C[i] if C[i] < D.inf else 'INF')
