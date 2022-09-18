# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
import sys
from library.dinic import Dinic

input = sys.stdin.readline

N, M = map(int, input().split())
dinic = Dinic(N)
for _ in range(M):
    u, v, cap = map(int, input().split())
    dinic.add_edge(u, v, cap)
print(dinic.flow(0, N - 1))
