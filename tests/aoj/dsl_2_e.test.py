# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_E
import sys
from library.dual_segment_tree import DualSegTree

input = sys.stdin.readline

N, Q = map(int, input().split())
dst = DualSegTree(N, lambda a, b: a + b, 0)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        s, t, x = q
        s -= 1
        dst.query(s, t, x)
    else:
        i, = q
        i -= 1
        print(dst.get(i))
