# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum
import sys
import bisect
from library.wavelet_matrix import WaveletMatrix

input = sys.stdin.readline

N, Q = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]
P.sort(key=lambda x: x[0])
X = []
A = []
W = []
for x, y, w in P:
    X.append(x)
    A.append(y)
    W.append(w)

WM = WaveletMatrix(A, W)
for _ in range(Q):
    lx, ly, rx, ry = map(int, input().split())
    l, r = bisect.bisect_left(X, lx), bisect.bisect_left(X, rx)
    print(WM.range_sum(l, r, ly, ry))
