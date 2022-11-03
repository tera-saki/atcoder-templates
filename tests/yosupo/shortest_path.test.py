# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
import sys
from library.dijkstra import Dijkstra

input = sys.stdin.readline

N, M, s, t = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E[a].append((c, b))

solver = Dijkstra(N, E, start=s)
cost = solver.get_cost(t)
if cost == solver.inf:
    print(-1)
    exit()
p = solver.get_path(t)
print(cost, len(p) - 1)
for a, b in zip(p[:-1], p[1:]):
    print(a, b)
