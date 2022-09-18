# https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/GRL_4_B/judge/6940421/Python3
import sys
from library.topological_sort import TopologicalSort

input = sys.stdin.readline

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)

ret = TopologicalSort(N, E).sort()
print(*ret, sep='\n')
