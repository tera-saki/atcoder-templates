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
    path: tests/yosupo/rectangle_sum.test.py
    title: tests/yosupo/rectangle_sum.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/static_range_frequency.test.py
    title: tests/yosupo/static_range_frequency.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yuki/738.test.py
    title: tests/yuki/738.test.py
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
  code: "from typing import List\nimport bisect\n\n\nclass BitVector:\n    # reference:\
    \ https://tiramister.net/blog/posts/bitvector/\n    TABLE = bytes([\n        0,\
    \ 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,\n        1, 2, 2, 3, 2, 3, 3, 4,\
    \ 2, 3, 3, 4, 3, 4, 4, 5,\n        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4,\
    \ 5,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        1, 2, 2,\
    \ 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4,\
    \ 4, 5, 4, 5, 5, 6,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n\
    \        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\n        1, 2, 2, 3,\
    \ 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4,\
    \ 5, 4, 5, 5, 6,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n  \
    \      3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\n        2, 3, 3, 4, 3,\
    \ 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6,\
    \ 5, 6, 6, 7,\n        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\n     \
    \   4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8,\n    ])\n\n    def __init__(self,\
    \ N):\n        self.cnum = (N + 255) >> 8\n\n        self.bit = bytearray(self.cnum\
    \ << 5)\n        self.chunk = [0] * (self.cnum + 1)\n        self.blocks = bytearray(self.cnum\
    \ << 5)\n\n        self.built = False\n\n    def set(self, pos):\n        self.bit[pos\
    \ >> 3] |= 1 << (pos & 7)\n\n    def access(self, pos):\n        return self.bit[pos\
    \ >> 3] >> (pos & 7) & 1\n\n    def popcount(self, num):\n        return self.TABLE[num]\n\
    \n    def build(self):\n        for i in range(self.cnum):\n            k = i\
    \ << 5\n            for j in range(31):\n                self.blocks[k + 1] =\
    \ self.blocks[k] + self.popcount(self.bit[k])\n                k += 1\n      \
    \      self.chunk[i + 1] = self.chunk[i] + self.blocks[k] + self.popcount(self.bit[k])\n\
    \        self.built = True\n\n    def rank(self, pos):\n        assert self.built\n\
    \        cpos, tmp = pos >> 8, pos & 255\n        bpos, offset = tmp >> 3, tmp\
    \ & 7\n\n        i = cpos << 5 | bpos\n        rest = self.bit[i] & ((1 << offset)\
    \ - 1)\n        return self.chunk[cpos] + self.blocks[i] + self.popcount(rest)\n\
    \n    def select(self, num):\n        \"\"\"return minimum i that satisfies rank(i)\
    \ = num\"\"\"\n        assert self.built\n        if num == 0:\n            return\
    \ 0\n        if self.rank(self.N) < num:\n            return -1\n\n        l =\
    \ -1\n        r = self.N\n        while r - l > 1:\n            c = (l + r) >>\
    \ 1\n            if self.rank(c) >= num:\n                r = c\n            else:\n\
    \                l = c\n        return r\n\n\nclass WaveletMatrix:\n    # reference:\
    \ https://miti-7.hatenablog.com/entry/2018/04/28/152259\n    def __init__(self,\
    \ A: List[int], weight: List[int] = None):\n        self.nums = sorted(set(A))\n\
    \        self.idx = {a: i for i, a in enumerate(self.nums)}\n        self.A =\
    \ [self.idx[a] for a in A]\n\n        self.digit = (len(self.nums) - 1).bit_length()\n\
    \        self.B = [None] * self.digit\n        self.offset = [None] * self.digit\n\
    \n        self.weight = weight\n        if self.weight:\n            self.S =\
    \ [[0 for _ in range(len(self.A) + 1)] for _ in range(self.digit + 1)]\n     \
    \       for i, a in enumerate(self.A):\n                self.S[self.digit][i +\
    \ 1] = self.S[self.digit][i] + self.weight[i]\n\n        if self.weight:\n   \
    \         T = list(zip(self.A, self.weight))\n            for k in range(self.digit)[::-1]:\n\
    \                self.B[k] = BitVector(len(T) + 1)\n                zeros = []\n\
    \                ones = []\n                for i, (a, w) in enumerate(T):\n \
    \                   if a >> k & 1:\n                        self.B[k].set(i)\n\
    \                        ones.append((a, w))\n                    else:\n    \
    \                    zeros.append((a, w))\n                self.B[k].build()\n\
    \                self.offset[k] = len(zeros)\n                T = zeros + ones\n\
    \                for i, (a, w) in enumerate(T):\n                    self.S[k][i\
    \ + 1] = self.S[k][i] + w\n        else:\n            T = self.A\n           \
    \ for k in range(self.digit)[::-1]:\n                self.B[k] = BitVector(len(T)\
    \ + 1)\n                zeros = []\n                ones = []\n              \
    \  for i, a in enumerate(T):\n                    if a >> k & 1:\n           \
    \             self.B[k].set(i)\n                        ones.append(a)\n     \
    \               else:\n                        zeros.append(a)\n             \
    \   self.B[k].build()\n                self.offset[k] = len(zeros)\n         \
    \       T = zeros + ones\n\n    def access(self, i: int):\n        \"\"\"return\
    \ i-th value\"\"\"\n        ret = 0\n        cur = i\n        for k in range(self.digit)[::-1]:\n\
    \            if self.B[k].access(cur):\n                ret |= (1 << k)\n    \
    \            cur = self.B[k].rank(cur) + self.offset[k]\n            else:\n \
    \               cur -= self.B[k].rank(cur)\n        return self.nums[ret]\n\n\
    \    def rank(self, l: int, r: int, x: int):\n        \"\"\"return the number\
    \ of x's in [l, r) range\"\"\"\n        x = self.idx.get(x)\n        if x is None:\n\
    \            return 0\n        for k in range(self.digit)[::-1]:\n           \
    \ if x >> k & 1:\n                l = self.B[k].rank(l) + self.offset[k]\n   \
    \             r = self.B[k].rank(r) + self.offset[k]\n            else:\n    \
    \            l -= self.B[k].rank(l)\n                r -= self.B[k].rank(r)\n\
    \        return r - l\n\n    def quantile(self, l: int, r: int, n: int):\n   \
    \     \"\"\"return n-th (0-indexed) smallest value in [l, r) range\"\"\"\n   \
    \     assert 0 <= n < r - l\n        ret = 0\n        for k in range(self.digit)[::-1]:\n\
    \            rank_l = self.B[k].rank(l)\n            rank_r = self.B[k].rank(r)\n\
    \            ones = rank_r - rank_l\n            zeros = r - l - ones\n      \
    \      if zeros <= n:\n                ret |= 1 << k\n                l = rank_l\
    \ + self.offset[k]\n                r = rank_r + self.offset[k]\n            \
    \    n -= zeros\n            else:\n                l -= rank_l\n            \
    \    r -= rank_r\n        return self.nums[ret]\n\n    def rquantile(self, l:\
    \ int, r: int, n: int):\n        \"\"\"return n-th (0-indeed) largest value in\
    \ [l, r) range\"\"\"\n        return self.quantile(l, r, r - l - 1 - n)\n\n  \
    \  def range_freq(self, l: int, r: int, lower: int, upper: int):\n        \"\"\
    \"return the number of values s.t. lower <= x < upper in [l, r) range\"\"\"\n\
    \        if lower >= upper:\n            return 0\n        return self._range_freq_upper(l,\
    \ r, upper) - self._range_freq_upper(l, r, lower)\n\n    def prev_value(self,\
    \ l: int, r: int, upper: int):\n        \"\"\"return maximum x s.t. x < upper\
    \ in [l, r) range if exist, otherwise None\"\"\"\n        cnt = self._range_freq_upper(l,\
    \ r, upper)\n        if cnt == 0:\n            return None\n        return self.quantile(l,\
    \ r, cnt - 1)\n\n    def next_value(self, l: int, r: int, lower: int):\n     \
    \   \"\"\"return minimum x s.t. x >= lower in [l, r) range if exist, otherwise\
    \ None\"\"\"\n        cnt = self._range_freq_upper(l, r, lower)\n        if cnt\
    \ == r - l:\n            return None\n        return self.quantile(l, r, cnt)\n\
    \n    def range_sum(self, l: int, r: int, lower: int, upper: int):\n        \"\
    \"\"return sum of values s.t. lower <= x < upper in [l, r) range\n        must\
    \ be constructed with weight\n        \"\"\"\n        assert self.weight\n   \
    \     return self._range_sum_upper(l, r, upper) - self._range_sum_upper(l, r,\
    \ lower)\n\n    def range_nsmallest_sum(self, l: int, r: int, n: int):\n     \
    \   \"\"\"return sum of the first n (**1-indexed**) values ordered by ascending\
    \ order in [l, r) range\n        must be constructed with weight\n        \"\"\
    \"\n        assert self.weight\n        if l >= r:\n            return 0\n   \
    \     if self.digit == 0:\n            return self.nums[0] * n\n        ret =\
    \ 0\n        for k in range(self.digit)[::-1]:\n            rank_l = self.B[k].rank(l)\n\
    \            rank_r = self.B[k].rank(r)\n            ones = rank_r - rank_l\n\
    \            zeros = r - l - ones\n            if zeros <= n:\n              \
    \  ret += self._get_internal_sum(k, l - rank_l, r - rank_r)\n                l\
    \ = rank_l + self.offset[k]\n                r = rank_r + self.offset[k]\n   \
    \             n -= zeros\n                if n == 0:\n                    return\
    \ ret\n            else:\n                l -= rank_l\n                r -= rank_r\n\
    \        ret += self._get_internal_sum(0, l, l + n)\n        return ret\n\n  \
    \  def range_nlargest_sum(self, l: int, r: int, n: int):\n        \"\"\"return\
    \ sum of the first n (**1-indexed**) values ordered by descending order in [l,\
    \ r) range\n        must be constructed with weight\n        \"\"\"\n        assert\
    \ self.weight\n        return self._get_internal_sum(self.digit, l, r) - self.range_nsmallest_sum(l,\
    \ r, r - l - n)\n\n    def _range_freq_upper(self, l: int, r: int, upper: int):\n\
    \        \"\"\"return the number of values s.t. x < upper in [l, r) range\"\"\"\
    \n        if l >= r:\n            return 0\n        if upper > self.nums[-1]:\n\
    \            return r - l\n        if upper <= self.nums[0]:\n            return\
    \ 0\n        upper = bisect.bisect_left(self.nums, upper)\n        ret = 0\n \
    \       for k in range(self.digit)[::-1]:\n            rank_l = self.B[k].rank(l)\n\
    \            rank_r = self.B[k].rank(r)\n            ones = rank_r - rank_l\n\
    \            zeros = r - l - ones\n            if upper >> k & 1:\n          \
    \      ret += zeros\n                l = rank_l + self.offset[k]\n           \
    \     r = rank_r + self.offset[k]\n            else:\n                l -= rank_l\n\
    \                r -= rank_r\n        return ret\n\n    def _range_sum_upper(self,\
    \ l: int, r: int, upper: int):\n        \"\"\"return sum of values s.t. x < upper\
    \ in [l, r) range\"\"\"\n        if l >= r:\n            return 0\n        if\
    \ upper > self.nums[-1]:\n            return self._get_internal_sum(self.digit,\
    \ l, r)\n        if upper <= self.nums[0]:\n            return 0\n        upper\
    \ = bisect.bisect_left(self.nums, upper)\n        ret = 0\n        for k in range(self.digit)[::-1]:\n\
    \            rank_l = self.B[k].rank(l)\n            rank_r = self.B[k].rank(r)\n\
    \            ones = rank_r - rank_l\n            zero = r - l - ones\n       \
    \     if upper >> k & 1:\n                ret += self._get_internal_sum(k, l -\
    \ rank_l,  r - rank_r)\n                l = rank_l + self.offset[k]\n        \
    \        r = rank_r + self.offset[k]\n            else:\n                l -=\
    \ rank_l\n                r -= rank_r\n        return ret\n\n    def _get_internal_sum(self,\
    \ k: int, l: int, r: int):\n        return self.S[k][r] - self.S[k][l]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/wavelet_matrix.py
  requiredBy: []
  timestamp: '2023-01-10 19:45:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/1549.test.py
  - tests/yuki/738.test.py
  - tests/yosupo/static_range_frequency.test.py
  - tests/yosupo/rectangle_sum.test.py
  - tests/yosupo/range_kth_smallest.test.py
documentation_of: library/wavelet_matrix.py
layout: document
redirect_from:
- /library/library/wavelet_matrix.py
- /library/library/wavelet_matrix.py.html
title: library/wavelet_matrix.py
---
