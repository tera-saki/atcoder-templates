# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency
import sys
from library.wavelet_matrix import WaveletMatrix

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
WM = WaveletMatrix(A)
for _ in range(Q):
    l, r, x = map(int, input().split())
    print(WM.rank(l, r, x))
