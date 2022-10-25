# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/1595
import sys
from library.rerooting import Rerooting

input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    E[u].append((1, v))
    E[v].append((1, u))


def f(a, v, ch, cost):
    return a + 1


def g(a, v):
    return a


def merge(a, b):
    return max(a, b)


solver = Rerooting(N, E, f, g, merge, 0)
for i in range(N):
    print(2 * (N - 1) - solver.solve(i))
