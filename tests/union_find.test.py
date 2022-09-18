# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
import sys
from library.union_find import UnionFind

input = sys.stdin.readline

N, Q = map(int, input().split())
uf = UnionFind(N)
for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.unite(u, v)
    else:
        print(1 if uf.same(u, v) else 0)
