---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/binary_indexed_tree.py
    title: library/binary_indexed_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/point_add_rectangle_sum.test.py
    title: tests/yosupo/point_add_rectangle_sum.test.py
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
  code: "from typing import List, Tuple\nimport sys\nimport bisect\n\nfrom library.binary_indexed_tree\
    \ import BIT\n\n\nclass BitVector:\n    # reference: https://tiramister.net/blog/posts/bitvector/\n\
    \    TABLE = bytes([\n        0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,\n\
    \        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\n        1, 2, 2, 3,\
    \ 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4,\
    \ 5, 4, 5, 5, 6,\n        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\n  \
    \      2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        2, 3, 3, 4, 3,\
    \ 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6,\
    \ 5, 6, 6, 7,\n        1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,\n     \
    \   2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        2, 3, 3, 4, 3, 4,\
    \ 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5,\
    \ 6, 6, 7,\n        2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,\n        3,\
    \ 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,\n        3, 4, 4, 5, 4, 5, 5, 6,\
    \ 4, 5, 5, 6, 5, 6, 6, 7,\n        4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7,\
    \ 8,\n    ])\n\n    def __init__(self, N):\n        self.cnum = (N + 255) >> 8\n\
    \n        self.bit = bytearray(self.cnum << 5)\n        self.chunk = [0] * (self.cnum\
    \ + 1)\n        self.blocks = bytearray(self.cnum << 5)\n\n        self.built\
    \ = False\n\n    def set(self, pos):\n        self.bit[pos >> 3] |= 1 << (pos\
    \ & 7)\n\n    def access(self, pos):\n        return self.bit[pos >> 3] >> (pos\
    \ & 7) & 1\n\n    def popcount(self, num):\n        return self.TABLE[num]\n\n\
    \    def build(self):\n        for i in range(self.cnum):\n            k = i <<\
    \ 5\n            for j in range(31):\n                self.blocks[k + 1] = self.blocks[k]\
    \ + self.popcount(self.bit[k])\n                k += 1\n            self.chunk[i\
    \ + 1] = self.chunk[i] + self.blocks[k] + self.popcount(self.bit[k])\n       \
    \ self.built = True\n\n    def rank(self, pos):\n        assert self.built\n \
    \       cpos, tmp = pos >> 8, pos & 255\n        bpos, offset = tmp >> 3, tmp\
    \ & 7\n\n        i = cpos << 5 | bpos\n        rest = self.bit[i] & ((1 << offset)\
    \ - 1)\n        return self.chunk[cpos] + self.blocks[i] + self.popcount(rest)\n\
    \n    def select(self, num):\n        \"\"\"return minimum i that satisfies rank(i)\
    \ = num\"\"\"\n        assert self.built\n        if num == 0:\n            return\
    \ 0\n        if self.rank(self.N) < num:\n            return -1\n\n        l =\
    \ -1\n        r = self.N\n        while r - l > 1:\n            c = (l + r) >>\
    \ 1\n            if self.rank(c) >= num:\n                r = c\n            else:\n\
    \                l = c\n        return r\n\n\nclass WaveletMatrixPointAddRectangleSum:\n\
    \    # reference: https://miti-7.hatenablog.com/entry/2018/04/28/152259\n    def\
    \ __init__(self):\n        self.points = []\n        self.pidx = {}\n        self.X\
    \ = []\n        self.A = []\n        self.W = []\n        self.built = False\n\
    \n    def add_point(self, x, y, w=0):\n        self.points.append((x, y, w))\n\
    \n    def build(self):\n        self.points.sort(key=lambda x: x[0])\n       \
    \ for i, (x, y, w) in enumerate(self.points):\n            self.X.append(x)\n\
    \            self.A.append(y)\n            self.W.append(w)\n            self.pidx[(x,\
    \ y)] = i\n        self.nums = sorted(set(self.A))\n        self.aidx = {a: i\
    \ for i, a in enumerate(self.nums)}\n        self.A = [self.aidx[a] for a in self.A]\n\
    \        self.digit = (len(self.nums) - 1).bit_length()\n        self.B = [None]\
    \ * self.digit\n        self.offset = [None] * self.digit\n        self.S = [BIT(len(self.A))\
    \ for _ in range(self.digit)]\n\n        T = [i for i in range(len(self.A))]\n\
    \        for k in range(self.digit)[::-1]:\n            self.B[k] = BitVector(len(self.A)\
    \ + 1)\n            zeros = []\n            ones = []\n            for i, j in\
    \ enumerate(T):\n                if self.A[j] >> k & 1:\n                    self.B[k].set(i)\n\
    \                    ones.append(j)\n                else:\n                 \
    \   zeros.append(j)\n            self.B[k].build()\n            self.offset[k]\
    \ = len(zeros)\n            T = zeros + ones\n            self.S[k].build([self.W[j]\
    \ for j in T])\n\n        self.built = True\n\n    def add_value(self, x, y, a):\n\
    \        assert self.built\n        i = self.pidx[(x, y)]\n        v = self.aidx[y]\n\
    \        for k in range(self.digit)[::-1]:\n            if v >> k & 1:\n     \
    \           i = self.B[k].rank(i) + self.offset[k]\n            else:\n      \
    \          i -= self.B[k].rank(i)\n            self.S[k].add(i, a)\n\n    def\
    \ rectangle_sum(self, lx, ly, rx, ry):\n        assert self.built\n        l,\
    \ r = bisect.bisect_left(self.X, lx), bisect.bisect_left(self.X, rx)\n       \
    \ return self._range_sum_upper(l, r, ry) - self._range_sum_upper(l, r, ly)\n\n\
    \    def _range_sum_upper(self, l, r, upper):\n        \"\"\"return sum of values\
    \ s.t. x < upper in [l, r) range\"\"\"\n        upper = bisect.bisect_left(self.nums,\
    \ upper)\n        ret = 0\n        for k in range(self.digit)[::-1]:\n       \
    \     rank_l = self.B[k].rank(l)\n            rank_r = self.B[k].rank(r)\n   \
    \         if upper >> k & 1:\n                ret += self.S[k].range_sum(l - rank_l,\
    \ r - rank_r)\n                l = rank_l + self.offset[k]\n                r\
    \ = rank_r + self.offset[k]\n            else:\n                l -= rank_l\n\
    \                r -= rank_r\n        return ret\n"
  dependsOn:
  - library/binary_indexed_tree.py
  isVerificationFile: false
  path: library/point_add_rectangle_sum.py
  requiredBy: []
  timestamp: '2023-01-14 22:09:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/point_add_rectangle_sum.test.py
documentation_of: library/point_add_rectangle_sum.py
layout: document
redirect_from:
- /library/library/point_add_rectangle_sum.py
- /library/library/point_add_rectangle_sum.py.html
title: library/point_add_rectangle_sum.py
---
