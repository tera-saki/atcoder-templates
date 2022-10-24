# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/1595
import sys
from library.rerooting import Rerooting

input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    E[u].append(v)
    E[v].append(u)

solver = Rerooting(N, E, lambda a, _: a + 1, lambda a, _: a, max, 0)
for i in range(N):
    print(2 * (N - 1) - solver.solve(i))
