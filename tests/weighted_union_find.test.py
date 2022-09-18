# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_1_B
import sys
from library.weighted_union_find import WeightedUnionFind

input = sys.stdin.readline

N, Q = map(int, input().split())
uf = WeightedUnionFind(N)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        x, y, z = q
        uf.merge(x, y, z)
    else:
        x, y = q
        res = uf.diff(x, y)
        print(res if res is not None else '?')
