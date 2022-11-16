# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C
import sys
from library.bfs import BFS

input = sys.stdin.readline

N = int(input())
E = []
for _ in range(N):
    u, k, *V = map(int, input().split())
    E.append([v - 1 for v in V])

solver = BFS(N, E)
for i in range(N):
    c = solver.get_cost(i)
    print(i + 1, c if c < solver.inf else -1)
