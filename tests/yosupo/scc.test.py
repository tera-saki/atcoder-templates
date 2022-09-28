# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
from library.scc import SCC

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
scc = SCC(N, E)

print(scc.c_num)
for i in range(scc.c_num):
    print(len(scc.C[i]), *scc.C[i])
