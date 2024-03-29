import random


class RollingHash:
    # reference: https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
    MSK30 = (1 << 30) - 1
    MSK31 = (1 << 31) - 1
    MOD = (1 << 61) - 1
    MSK61 = MOD

    def __init__(self, S, base=None):
        self.h = [0] * (len(S) + 1)
        self.p = [1] * (len(S) + 1)

        if base is None:
            self.base = random.randint(2, self.MOD - 2)
        else:
            self.base = base

        for i in range(len(S)):
            self.h[i + 1] = self._mod(self._mul(self.h[i], self.base) + ord(S[i]))
        for i in range(len(S)):
            self.p[i + 1] = self._mul(self.p[i], self.base)

    # S[l:r]
    def get(self, l, r):
        """return hash of S[l:r]"""
        return self._mod(self.h[r] - self._mul(self.h[l], self.p[r - l]))

    def merge(self, l1, r1, l2, r2):
        """return hash of S[l1:r1] + S[l2:r2]"""
        h1 = self.get(l1, r1)
        h2 = self.get(l2, r2)
        return self._mod(self._mul(h1, self.p[r2 - l2]) + h2)

    def _mul(self, a, b):
        au, ad = a >> 31, a & self.MSK31
        bu, bd = b >> 31, b & self.MSK31
        mid = ad * bu + au * bd
        midu, midd = mid >> 30, mid & self.MSK30
        return self._mod(au * bu * 2 + midu + (midd << 31) + ad * bd)

    def _mod(self, x):
        xu, xd = x >> 61, x & self.MSK61
        ret = xu + xd
        if ret >= self.MOD:
            ret -= self.MOD
        return ret
