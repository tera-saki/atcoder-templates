# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
import sys
from library.lowlink import Lowlink

input = sys.stdin.readline

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    E[s].append(t)
    E[t].append(s)

points = Lowlink(N, E).articulation_points()
for p in points:
    print(p)
