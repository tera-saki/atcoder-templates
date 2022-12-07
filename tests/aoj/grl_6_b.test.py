# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
import sys
from library.primal_dual import PrimalDual

input = sys.stdin.readline

N, M, F = map(int, input().split())
solver = PrimalDual(N)
for _ in range(M):
    u, v, cap, cost = map(int, input().split())
    solver.add_edge(u, v, cap, cost)
ans = solver.flow(0, N - 1, F)
print(ans if ans is not None else -1)
