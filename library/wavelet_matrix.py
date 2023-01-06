import bisect


class BitVector:
    # reference: https://tiramister.net/blog/posts/bitvector/
    # (reference implemention is succinct, but this implemention is not succinct.)
    def __init__(self, N):
        self.N = N
        self.block_num = (N + 31) >> 5
        self.bit = [0] * self.block_num
        self.sum = [0] * self.block_num

        self.built = False

    def set(self, pos):
        self.bit[pos >> 5] |= 1 << (pos & 31)

    def build(self):
        assert not self.built
        for i in range(1, self.block_num):
            self.sum[i] = self.sum[i - 1] + self.popcount(self.bit[i - 1])
        self.built = True

    def access(self, pos):
        """return pos-th bit"""
        return self.bit[pos >> 5] >> (pos & 31) & 1

    def rank(self, pos):
        """count 1's in [0, pos) range"""
        assert self.built
        i = pos >> 5
        offset = pos & 31
        return self.sum[i] + self.popcount(self.bit[i] & ((1 << offset) - 1))

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

    def popcount(self, n):
        c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
        c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
        c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
        c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
        c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
        return c


class WaveletMatrix:
    # reference: https://miti-7.hatenablog.com/entry/2018/04/28/152259
    def __init__(self, A):
        self.nums = sorted(set(A))
        self.idx = {a: i for i, a in enumerate(self.nums)}
        self.A = [self.idx[a] for a in A]

        self.digit = (len(self.nums) - 1).bit_length()
        self.B = [None] * self.digit
        self.offset = [None] * self.digit
        self.start_index = {}

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
        for i, a in enumerate(T):
            self.start_index.setdefault(a, i)

    def access(self, i):
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

    def rank(self, i, x):
        """return the number of x's in [0, i) range"""
        x = self.idx.get(x)
        if x is None:
            return 0
        for k in range(self.digit)[::-1]:
            if x >> k & 1:
                i = self.B[k].rank(i) + self.offset[k]
            else:
                i -= self.B[k].rank(i)
        return i - self.start_index[x]

    def quantile(self, l, r, n):
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

    def range_freq(self, l, r, lower, upper):
        """return the number of values s.t. lower <= x < upper"""
        return self.range_freq_upper(l, r, upper) - self.range_freq_upper(l, r, lower)

    def range_freq_upper(self, l, r, upper):
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
