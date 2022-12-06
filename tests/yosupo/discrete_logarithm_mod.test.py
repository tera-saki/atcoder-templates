# verification-helper: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod
import sys
from library.math import solve_discrete_logarithm

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y, m = map(int, input().split())
    ans = solve_discrete_logarithm(x, y, m)
    print(ans if ans is not None else -1)
