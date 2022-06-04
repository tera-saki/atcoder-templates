import sys
from collections import defaultdict


class Osa_k:
    # N以下の整数を素因数分解 O(NlogN)
    def __init__(self, N):
        self.min_factor = [i for i in range(N + 1)]
        for i in range(2, N + 1):
            if i * i > N:
                break
            if self.min_factor[i] == i:
                for j in range(2, N + 1):
                    if i * j > N:
                        break
                    if self.min_factor[i * j] > i:
                        self.min_factor[i * j] = i

    def factors(self, n):
        f = []
        while n > 1:
            f.append(self.min_factor[n])
            n //= self.min_factor[n]
        return f


# https://yukicoder.me/problems/no/1006
X = int(input())
osa_k = Osa_k(X)
f = [0] * X
for i in range(1, X):
    factors = osa_k.factors(i)
    D = defaultdict(int)
    for factor in factors:
        D[factor] += 1
    d = 1
    for v in D.values():
        d *= (v + 1)
    f[i] = i - d
v = [1 << 30] * X
for i in range(1, X):
    v[i] = abs(f[i] - f[X - i])
minv = min(v)
for i in range(1, X):
    if v[i] == minv:
        print(i, X - i)
