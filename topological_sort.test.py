# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_B
import sys
from topological_sort import TopologicalSort

input = sys.stdin.readline

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)

_, ret = TopologicalSort(N, E).sort()
print(*ret, sep='\n')
