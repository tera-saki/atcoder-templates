# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/1549
import sys
from library.wavelet_matrix import WaveletMatrix

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
WM = WaveletMatrix(A)
Q = int(input())
for _ in range(Q):
    l, r, d = map(int, input().split())
    pre = WM.prev_value(l, r + 1, d)
    nxt = WM.next_value(l, r + 1, d)
    if pre is None:
        print(abs(nxt - d))
    elif nxt is None:
        print(abs(pre - d))
    else:
        print(min(abs(pre - d), abs(nxt - d)))
