# verification-helper: PROBLEM https://yukicoder.me/problems/no/738
import sys
from library.wavelet_matrix import WaveletMatrix

input = sys.stdin.readline


N, K = map(int, input().split())
A = list(map(int, input().split()))
W = WaveletMatrix(A, A)
INF = 1 << 50
ans = INF
for i in range(N - K + 1):
    v = W.range_nlargest_sum(i, i + K, K // 2) - W.range_nsmallest_sum(i, i + K, K // 2)
    ans = min(ans, v)
print(ans)
