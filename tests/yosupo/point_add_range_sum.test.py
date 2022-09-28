# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
import sys
from library.segment_tree import SegTree

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

st = SegTree(N, lambda a, b: a + b, 0)
st.build(A)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        st.add(x, y)
    else:
        print(st.query(x, y))
