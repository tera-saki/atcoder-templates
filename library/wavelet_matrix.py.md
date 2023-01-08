---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/1549.test.py
    title: tests/aoj/1549.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/range_kth_smallest.test.py
    title: tests/yosupo/range_kth_smallest.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/static_range_frequency.test.py
    title: tests/yosupo/static_range_frequency.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://miti-7.hatenablog.com/entry/2018/04/28/152259
    - https://tiramister.net/blog/posts/bitvector/
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import bisect\n\n\nclass BitVector:\n    # reference: https://tiramister.net/blog/posts/bitvector/\n\
    \    # (reference implemention is succinct, but this implemention is not succinct.)\n\
    \    def __init__(self, N):\n        self.N = N\n        self.block_num = (N +\
    \ 31) >> 5\n        self.bit = [0] * self.block_num\n        self.sum = [0] *\
    \ self.block_num\n\n        self.built = False\n\n    def set(self, pos):\n  \
    \      self.bit[pos >> 5] |= 1 << (pos & 31)\n\n    def build(self):\n       \
    \ assert not self.built\n        for i in range(1, self.block_num):\n        \
    \    self.sum[i] = self.sum[i - 1] + self.popcount(self.bit[i - 1])\n        self.built\
    \ = True\n\n    def access(self, pos):\n        \"\"\"return pos-th bit\"\"\"\n\
    \        return self.bit[pos >> 5] >> (pos & 31) & 1\n\n    def rank(self, pos):\n\
    \        \"\"\"count 1's in [0, pos) range\"\"\"\n        assert self.built\n\
    \        i = pos >> 5\n        offset = pos & 31\n        return self.sum[i] +\
    \ self.popcount(self.bit[i] & ((1 << offset) - 1))\n\n    def select(self, num):\n\
    \        \"\"\"return minimum i that satisfies rank(i) = num\"\"\"\n        assert\
    \ self.built\n        if num == 0:\n            return 0\n        if self.rank(self.N)\
    \ < num:\n            return -1\n\n        l = -1\n        r = self.N\n      \
    \  while r - l > 1:\n            c = (l + r) >> 1\n            if self.rank(c)\
    \ >= num:\n                r = c\n            else:\n                l = c\n \
    \       return r\n\n    def popcount(self, n):\n        c = (n & 0x5555555555555555)\
    \ + ((n >> 1) & 0x5555555555555555)\n        c = (c & 0x3333333333333333) + ((c\
    \ >> 2) & 0x3333333333333333)\n        c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4)\
    \ & 0x0f0f0f0f0f0f0f0f)\n        c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)\n\
    \        c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)\n   \
    \     return c\n\n\nclass WaveletMatrix:\n    # reference: https://miti-7.hatenablog.com/entry/2018/04/28/152259\n\
    \    def __init__(self, A):\n        self.nums = sorted(set(A))\n        self.idx\
    \ = {a: i for i, a in enumerate(self.nums)}\n        self.A = [self.idx[a] for\
    \ a in A]\n\n        self.digit = (len(self.nums) - 1).bit_length()\n        self.B\
    \ = [None] * self.digit\n        self.offset = [None] * self.digit\n        self.start_index\
    \ = [-1] * len(self.nums)\n\n        T = self.A\n        for k in range(self.digit)[::-1]:\n\
    \            self.B[k] = BitVector(len(T) + 1)\n            zeros = []\n     \
    \       ones = []\n            for i, a in enumerate(T):\n                if a\
    \ >> k & 1:\n                    self.B[k].set(i)\n                    ones.append(a)\n\
    \                else:\n                    zeros.append(a)\n            self.B[k].build()\n\
    \            self.offset[k] = len(zeros)\n            T = zeros + ones\n     \
    \   for i, a in enumerate(T):\n            if self.start_index[a] < 0:\n     \
    \           self.start_index[a] = i\n\n    def access(self, i):\n        \"\"\"\
    return i-th value\"\"\"\n        ret = 0\n        cur = i\n        for k in range(self.digit)[::-1]:\n\
    \            if self.B[k].access(cur):\n                ret |= (1 << k)\n    \
    \            cur = self.B[k].rank(cur) + self.offset[k]\n            else:\n \
    \               cur -= self.B[k].rank(cur)\n        return self.nums[ret]\n\n\
    \    def rank(self, i, x):\n        \"\"\"return the number of x's in [0, i) range\"\
    \"\"\n        x = self.idx.get(x)\n        if x is None:\n            return 0\n\
    \        for k in range(self.digit)[::-1]:\n            if x >> k & 1:\n     \
    \           i = self.B[k].rank(i) + self.offset[k]\n            else:\n      \
    \          i -= self.B[k].rank(i)\n        return i - self.start_index[x]\n\n\
    \    def quantile(self, l, r, n):\n        \"\"\"return n-th (0-indexed) smallest\
    \ value in [l, r) range\"\"\"\n        assert 0 <= n < r - l\n        ret = 0\n\
    \        for k in range(self.digit)[::-1]:\n            rank_l = self.B[k].rank(l)\n\
    \            rank_r = self.B[k].rank(r)\n            ones = rank_r - rank_l\n\
    \            zeros = r - l - ones\n            if zeros <= n:\n              \
    \  ret |= 1 << k\n                l = rank_l + self.offset[k]\n              \
    \  r = rank_r + self.offset[k]\n                n -= zeros\n            else:\n\
    \                l -= rank_l\n                r -= rank_r\n        return self.nums[ret]\n\
    \n    def range_freq(self, l, r, lower, upper):\n        \"\"\"return the number\
    \ of values s.t. lower <= x < upper\"\"\"\n        return self.range_freq_upper(l,\
    \ r, upper) - self.range_freq_upper(l, r, lower)\n\n    def prev_value(self, l,\
    \ r, upper):\n        \"\"\"return maximum x s.t. x < upper in [l, r) range if\
    \ exist, otherwise None\"\"\"\n        cnt = self.range_freq_upper(l, r, upper)\n\
    \        if cnt == 0:\n            return None\n        return self.quantile(l,\
    \ r, cnt - 1)\n\n    def next_value(self, l, r, lower):\n        \"\"\"return\
    \ minimum x s.t. x >= lower in [l, r) range if exist, otherwise None\"\"\"\n \
    \       cnt = self.range_freq_upper(l, r, lower)\n        if cnt == r - l:\n \
    \           return None\n        return self.quantile(l, r, cnt)\n\n    def range_freq_upper(self,\
    \ l, r, upper):\n        \"\"\"return the number of values s.t. x < upper in [l,\
    \ r) range\"\"\"\n        if l >= r:\n            return 0\n        if upper >\
    \ self.nums[-1]:\n            return r - l\n        if upper <= self.nums[0]:\n\
    \            return 0\n        upper = bisect.bisect_left(self.nums, upper)\n\
    \        ret = 0\n        for k in range(self.digit)[::-1]:\n            rank_l\
    \ = self.B[k].rank(l)\n            rank_r = self.B[k].rank(r)\n            ones\
    \ = rank_r - rank_l\n            zeros = r - l - ones\n            if upper >>\
    \ k & 1:\n                ret += zeros\n                l = rank_l + self.offset[k]\n\
    \                r = rank_r + self.offset[k]\n            else:\n            \
    \    l -= rank_l\n                r -= rank_r\n        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: library/wavelet_matrix.py
  requiredBy: []
  timestamp: '2023-01-08 11:42:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/1549.test.py
  - tests/yosupo/static_range_frequency.test.py
  - tests/yosupo/range_kth_smallest.test.py
documentation_of: library/wavelet_matrix.py
layout: document
redirect_from:
- /library/library/wavelet_matrix.py
- /library/library/wavelet_matrix.py.html
title: library/wavelet_matrix.py
---
