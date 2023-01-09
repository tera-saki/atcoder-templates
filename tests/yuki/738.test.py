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
    med = W.quantile(i, i + K, K // 2)
    upper_sum = W.range_sum(i, i + K, med, INF) - med * W.range_freq(i, i + K, med, INF)
    lower_sum = med * W.range_freq(i, i + K, 0, med) - W.range_sum(i, i + K, 0, med)
    ans = min(ans, upper_sum + lower_sum)
print(ans)
