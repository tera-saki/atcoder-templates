# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest
import sys
from library.wavelet_matrix import WaveletMatrix

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
WM = WaveletMatrix(A)
for _ in range(Q):
    l, r, k = map(int, input().split())
    print(WM.quantile(l, r, k))
