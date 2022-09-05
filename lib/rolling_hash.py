import random


class RollingHash:
    def __init__(self, S, mod=None, base=None):
        self.h = [0] * (len(S) + 1)
        self.p = [1] * (len(S) + 1)
        if mod is None:
            self.mod = (1 << 61) - 1
        if base is None:
            self.base = random.randint(1, self.mod - 1)

        for i in range(len(S)):
            self.h[i + 1] = (self.h[i] * self.base + ord(S[i])) % self.mod
        for i in range(len(S)):
            self.p[i + 1] = self.p[i] * self.base % self.mod

    # S[l:r]
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.mod
