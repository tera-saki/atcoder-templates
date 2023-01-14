from typing import List, Tuple
import sys
import bisect

from library.binary_indexed_tree import BIT


class BitVector:
    # reference: https://tiramister.net/blog/posts/bitvector/
    TABLE = bytes([
        0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
        4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8,
    ])

    def __init__(self, N):
        self.cnum = (N + 255) >> 8

        self.bit = bytearray(self.cnum << 5)
        self.chunk = [0] * (self.cnum + 1)
        self.blocks = bytearray(self.cnum << 5)

        self.built = False

    def set(self, pos):
        self.bit[pos >> 3] |= 1 << (pos & 7)

    def access(self, pos):
        return self.bit[pos >> 3] >> (pos & 7) & 1

    def popcount(self, num):
        return self.TABLE[num]

    def build(self):
        for i in range(self.cnum):
            k = i << 5
            for j in range(31):
                self.blocks[k + 1] = self.blocks[k] + self.popcount(self.bit[k])
                k += 1
            self.chunk[i + 1] = self.chunk[i] + self.blocks[k] + self.popcount(self.bit[k])
        self.built = True

    def rank(self, pos):
        assert self.built
        cpos, tmp = pos >> 8, pos & 255
        bpos, offset = tmp >> 3, tmp & 7

        i = cpos << 5 | bpos
        rest = self.bit[i] & ((1 << offset) - 1)
        return self.chunk[cpos] + self.blocks[i] + self.popcount(rest)

    def select(self, num):
        """return minimum i that satisfies rank(i) = num"""
        assert self.built
        if num == 0:
            return 0
        if self.rank(self.N) < num:
            return -1

        l = -1
        r = self.N
        while r - l > 1:
            c = (l + r) >> 1
            if self.rank(c) >= num:
                r = c
            else:
                l = c
        return r


class WaveletMatrixPointAddRectangleSum:
    # reference: https://miti-7.hatenablog.com/entry/2018/04/28/152259
    def __init__(self):
        self.points = []
        self.pidx = {}
        self.X = []
        self.A = []
        self.W = []
        self.built = False

    def add_point(self, x, y, w=0):
        self.points.append((x, y, w))

    def build(self):
        self.points.sort(key=lambda x: x[0])
        for i, (x, y, w) in enumerate(self.points):
            self.X.append(x)
            self.A.append(y)
            self.W.append(w)
            self.pidx[(x, y)] = i
        self.nums = sorted(set(self.A))
        self.aidx = {a: i for i, a in enumerate(self.nums)}
        self.A = [self.aidx[a] for a in self.A]
        self.digit = (len(self.nums) - 1).bit_length()
        self.B = [None] * self.digit
        self.offset = [None] * self.digit
        self.S = [BIT(len(self.A)) for _ in range(self.digit)]

        T = [i for i in range(len(self.A))]
        for k in range(self.digit)[::-1]:
            self.B[k] = BitVector(len(self.A) + 1)
            zeros = []
            ones = []
            for i, j in enumerate(T):
                if self.A[j] >> k & 1:
                    self.B[k].set(i)
                    ones.append(j)
                else:
                    zeros.append(j)
            self.B[k].build()
            self.offset[k] = len(zeros)
            T = zeros + ones
            self.S[k].build([self.W[j] for j in T])

        self.built = True

    def add_value(self, x, y, a):
        assert self.built
        i = self.pidx[(x, y)]
        v = self.aidx[y]
        for k in range(self.digit)[::-1]:
            if v >> k & 1:
                i = self.B[k].rank(i) + self.offset[k]
            else:
                i -= self.B[k].rank(i)
            self.S[k].add(i, a)

    def rectangle_sum(self, lx, ly, rx, ry):
        assert self.built
        l, r = bisect.bisect_left(self.X, lx), bisect.bisect_left(self.X, rx)
        return self._range_sum_upper(l, r, ry) - self._range_sum_upper(l, r, ly)

    def _range_sum_upper(self, l, r, upper):
        """return sum of values s.t. x < upper in [l, r) range"""
        upper = bisect.bisect_left(self.nums, upper)
        ret = 0
        for k in range(self.digit)[::-1]:
            rank_l = self.B[k].rank(l)
            rank_r = self.B[k].rank(r)
            if upper >> k & 1:
                ret += self.S[k].range_sum(l - rank_l, r - rank_r)
                l = rank_l + self.offset[k]
                r = rank_r + self.offset[k]
            else:
                l -= rank_l
                r -= rank_r
        return ret
