# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/0366
import sys
from library.scc import SCC

input = sys.stdin.readline


N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    E[s].append(t)

solver = SCC(N, E)
C, NE = solver.to_dag()
if len(C) == 1:
    print(0)
else:
    IN = [0] * len(C)
    OUT = [0] * len(C)
    for i in range(len(C)):
        for j in NE[i]:
            IN[j] += 1
            OUT[i] += 1
    print(max(IN.count(0), OUT.count(0)))
