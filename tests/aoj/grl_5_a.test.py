# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
import sys
from library.rerooting import Rerooting

input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t, w = map(int, input().split())
    E[s].append((w, t))
    E[t].append((w, s))


def f(a, v, ch, cost):
    return a + cost


def g(a, v):
    return a


def merge(a, b):
    return max(a, b)


solver = Rerooting(N, E, f, g, merge, 0)
ans = 0
for i in range(N):
    v = solver.solve(i)
    ans = max(ans, v)
print(ans)
