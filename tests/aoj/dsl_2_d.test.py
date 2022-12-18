# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D
import sys
from library.dual_segment_tree import DualSegTree

input = sys.stdin.readline

N, Q = map(int, input().split())
dst = DualSegTree(N, lambda a, b: b, (1 << 31) - 1)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        a, b, x = q
        dst.query(a, b + 1, x)
    else:
        i, = q
        print(dst.get(i))
