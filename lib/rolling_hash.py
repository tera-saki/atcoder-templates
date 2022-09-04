import sys
import random

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


class RollingHash:
    def __init__(self, S):
        self.h = [0] * (len(S) + 1)
        self.p = [1] * (len(S) + 1)
        self.mod = (1 << 61) - 1
        self.base = random.randint(1, self.mod - 1)

        for i in range(len(S)):
            self.h[i + 1] = (self.h[i] * self.base + ord(S[i])) % self.mod
        for i in range(len(S)):
            self.p[i + 1] = self.p[i] * self.base % self.mod

    # S[l:r]
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.mod


# https://atcoder.jp/contests/abc141/tasks/abc141_e
N = int(input())
S = input()[:-1]

RH = RollingHash(S)


def judge(length):
    hd = {}
    for i in range(N):
        if i + length > N:
            break
        h = RH.get(i, i + length)
        if hd.get(h) is not None:
            if hd[h] + length <= i:
                return True
        else:
            hd[h] = i
    return False


l = 0
r = len(S) + 1
while r - l > 1:
    c = (l + r) // 2
    if judge(c) is True:
        l = c
    else:
        r = c
print(l)
