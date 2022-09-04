# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

from scc import SCC

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
scc = SCC(N, E)

print(len(scc.C))
for i in range(len(scc.C)):
    print(len(scc.C[i]), *scc.C[i])