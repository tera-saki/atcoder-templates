# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
import sys
from library.bellman_ford import BellmanFord

input = sys.stdin.readline

N, M, start = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    s, t, d = map(int, input().split())
    E[s].append((d, t))

solver = BellmanFord(N, E, start=start)
cost = [solver.get_cost(i) for i in range(N)]
ans = []
for c in cost:
    if c == -solver.inf:
        print('NEGATIVE CYCLE')
        exit()
    ans.append(c if c < solver.inf else 'INF')
print(*ans, sep='\n')
