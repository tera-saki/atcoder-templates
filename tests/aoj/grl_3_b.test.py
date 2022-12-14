# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
import sys
from library.lowlink import Lowlink

input = sys.stdin.readline

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    E[s].append(t)
    E[t].append(s)

bridges = Lowlink(N, E).bridges()
bridges = [(s, t) if s < t else (t, s) for s, t in bridges]
for s, t in sorted(bridges):
    print(s, t)
