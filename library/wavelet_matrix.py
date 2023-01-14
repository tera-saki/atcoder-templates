from typing import List
import bisect


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


class WaveletMatrix:
    # reference: https://miti-7.hatenablog.com/entry/2018/04/28/152259
    def __init__(self, A: List[int], weight: List[int] = None):
        self.nums = sorted(set(A))
        self.idx = {a: i for i, a in enumerate(self.nums)}
        self.A = [self.idx[a] for a in A]

        self.digit = (len(self.nums) - 1).bit_length()
        self.B = [None] * self.digit
        self.offset = [None] * self.digit

        self.weight = weight
        if self.weight:
            self.S = [[0 for _ in range(len(self.A) + 1)] for _ in range(self.digit + 1)]
            for i, a in enumerate(self.A):
                self.S[self.digit][i + 1] = self.S[self.digit][i] + self.weight[i]

        if self.weight:
            T = list(zip(self.A, self.weight))
            for k in range(self.digit)[::-1]:
                self.B[k] = BitVector(len(T) + 1)
                zeros = []
                ones = []
                for i, (a, w) in enumerate(T):
                    if a >> k & 1:
                        self.B[k].set(i)
                        ones.append((a, w))
                    else:
                        zeros.append((a, w))
                self.B[k].build()
                self.offset[k] = len(zeros)
                T = zeros + ones
                for i, (a, w) in enumerate(T):
                    self.S[k][i + 1] = self.S[k][i] + w
        else:
            T = self.A
            for k in range(self.digit)[::-1]:
                self.B[k] = BitVector(len(T) + 1)
                zeros = []
                ones = []
                for i, a in enumerate(T):
                    if a >> k & 1:
                        self.B[k].set(i)
                        ones.append(a)
                    else:
                        zeros.append(a)
                self.B[k].build()
                self.offset[k] = len(zeros)
                T = zeros + ones

    def access(self, i: int):
        """return i-th value"""
        ret = 0
        cur = i
        for k in range(self.digit)[::-1]:
            if self.B[k].access(cur):
                ret |= (1 << k)
                cur = self.B[k].rank(cur) + self.offset[k]
            else:
                cur -= self.B[k].rank(cur)
        return self.nums[ret]

    def rank(self, l: int, r: int, x: int):
        """return the number of x's in [l, r) range"""
        x = self.idx.get(x)
        if x is None:
            return 0
        for k in range(self.digit)[::-1]:
            if x >> k & 1:
                l = self.B[k].rank(l) + self.offset[k]
                r = self.B[k].rank(r) + self.offset[k]
            else:
                l -= self.B[k].rank(l)
                r -= self.B[k].rank(r)
        return r - l

    def quantile(self, l: int, r: int, n: int):
        """return n-th (0-indexed) smallest value in [l, r) range"""
        assert 0 <= n < r - l
        ret = 0
        for k in range(self.digit)[::-1]:
            rank_l = self.B[k].rank(l)
            rank_r = self.B[k].rank(r)
            ones = rank_r - rank_l
            zeros = r - l - ones
            if zeros <= n:
                ret |= 1 << k
                l = rank_l + self.offset[k]
                r = rank_r + self.offset[k]
                n -= zeros
            else:
                l -= rank_l
                r -= rank_r
        return self.nums[ret]

    def rquantile(self, l: int, r: int, n: int):
        """return n-th (0-indeed) largest value in [l, r) range"""
        return self.quantile(l, r, r - l - 1 - n)

    def range_freq(self, l: int, r: int, lower: int, upper: int):
        """return the number of values s.t. lower <= x < upper in [l, r) range"""
        if lower >= upper:
            return 0
        return self._range_freq_upper(l, r, upper) - self._range_freq_upper(l, r, lower)

    def prev_value(self, l: int, r: int, upper: int):
        """return maximum x s.t. x < upper in [l, r) range if exist, otherwise None"""
        cnt = self._range_freq_upper(l, r, upper)
        if cnt == 0:
            return None
        return self.quantile(l, r, cnt - 1)

    def next_value(self, l: int, r: int, lower: int):
        """return minimum x s.t. x >= lower in [l, r) range if exist, otherwise None"""
        cnt = self._range_freq_upper(l, r, lower)
        if cnt == r - l:
            return None
        return self.quantile(l, r, cnt)

    def range_sum(self, l: int, r: int, lower: int, upper: int):
        """return sum of values s.t. lower <= x < upper in [l, r) range
        must be constructed with weight
        """
        assert self.weight
        return self._range_sum_upper(l, r, upper) - self._range_sum_upper(l, r, lower)

    def range_nsmallest_sum(self, l: int, r: int, n: int):
        """return sum of the first n (**1-indexed**) values ordered by ascending order in [l, r) range
        must be constructed with weight
        """
        assert self.weight
        if l >= r:
            return 0
        if self.digit == 0:
            return self.nums[0] * n
        ret = 0
        for k in range(self.digit)[::-1]:
            rank_l = self.B[k].rank(l)
            rank_r = self.B[k].rank(r)
            ones = rank_r - rank_l
            zeros = r - l - ones
            if zeros <= n:
                ret += self._get_internal_sum(k, l - rank_l, r - rank_r)
                l = rank_l + self.offset[k]
                r = rank_r + self.offset[k]
                n -= zeros
                if n == 0:
                    return ret
            else:
                l -= rank_l
                r -= rank_r
        ret += self._get_internal_sum(0, l, l + n)
        return ret

    def range_nlargest_sum(self, l: int, r: int, n: int):
        """return sum of the first n (**1-indexed**) values ordered by descending order in [l, r) range
        must be constructed with weight
        """
        assert self.weight
        return self._get_internal_sum(self.digit, l, r) - self.range_nsmallest_sum(l, r, r - l - n)

    def _range_freq_upper(self, l: int, r: int, upper: int):
        """return the number of values s.t. x < upper in [l, r) range"""
        if l >= r:
            return 0
        if upper > self.nums[-1]:
            return r - l
        if upper <= self.nums[0]:
            return 0
        upper = bisect.bisect_left(self.nums, upper)
        ret = 0
        for k in range(self.digit)[::-1]:
            rank_l = self.B[k].rank(l)
            rank_r = self.B[k].rank(r)
            ones = rank_r - rank_l
            zeros = r - l - ones
            if upper >> k & 1:
                ret += zeros
                l = rank_l + self.offset[k]
                r = rank_r + self.offset[k]
            else:
                l -= rank_l
                r -= rank_r
        return ret

    def _range_sum_upper(self, l: int, r: int, upper: int):
        """return sum of values s.t. x < upper in [l, r) range"""
        if l >= r:
            return 0
        if upper > self.nums[-1]:
            return self._get_internal_sum(self.digit, l, r)
        if upper <= self.nums[0]:
            return 0
        upper = bisect.bisect_left(self.nums, upper)
        ret = 0
        for k in range(self.digit)[::-1]:
            rank_l = self.B[k].rank(l)
            rank_r = self.B[k].rank(r)
            if upper >> k & 1:
                ret += self._get_internal_sum(k, l - rank_l,  r - rank_r)
                l = rank_l + self.offset[k]
                r = rank_r + self.offset[k]
            else:
                l -= rank_l
                r -= rank_r
        return ret

    def _get_internal_sum(self, k: int, l: int, r: int):
        return self.S[k][r] - self.S[k][l]
