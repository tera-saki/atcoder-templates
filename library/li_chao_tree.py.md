---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/line_add_get_min.test.py
    title: tests/yosupo/line_add_get_min.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/segment_add_get_min.test.py
    title: tests/yosupo/segment_add_get_min.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://smijake3.hatenablog.com/entry/2018/06/16/144548
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple\n\n\nclass LiChaoTree:\n    # reference: https://smijake3.hatenablog.com/entry/2018/06/16/144548\n\
    \    def __init__(self, X: List[int], inf: int = int(1e20)):\n        for i in\
    \ range(len(X) - 1):\n            assert X[i] < X[i + 1]\n        self.X = X\n\
    \        self.idx = {x: i for i, x in enumerate(self.X)}\n        self.N = len(self.X)\n\
    \        self.K = (self.N - 1).bit_length()\n        self.size = 1 << self.K\n\
    \        self.data = [None] * (self.size << 1)\n        self.inf = inf\n     \
    \   for i in range(self.N, self.size):\n            self.X.append(self.inf)\n\n\
    \    def add_line(self, line: Tuple[int, int]) -> None:\n        \"\"\"add line\"\
    \"\"\n        self._add(line, 1, 0, self.size)\n\n    def add_line_segment(self,\
    \ line: Tuple[int, int], l: int, r: int) -> None:\n        \"\"\"add line segment\
    \ to [l, r) range\"\"\"\n        l, r = self.idx[l], self.idx[r]\n        l0,\
    \ r0 = l, r\n        l += self.size\n        r += self.size\n        sz = 1\n\
    \        while l < r:\n            if r & 1:\n                r -= 1\n       \
    \         r0 -= sz\n                self._add(line, r, r0, r0 + sz)\n        \
    \    if l & 1:\n                self._add(line, l, l0, l0 + sz)\n            \
    \    l += 1\n                l0 += sz\n            l >>= 1\n            r >>=\
    \ 1\n            sz <<= 1\n\n    def query(self, x: int) -> int:\n        i =\
    \ self.idx[x]\n        i += self.size\n        ret = self.inf\n        while i:\n\
    \            if self.data[i]:\n                a, b = self.data[i]\n         \
    \       ret = min(ret, a * x + b)\n            i >>= 1\n        return ret\n\n\
    \    def _add(self, line: Tuple[int, int], k: int, l: int, r: int) -> None:\n\
    \        while r - l:\n            if self.data[k] is None:\n                self.data[k]\
    \ = line\n                return\n            c = (l + r) >> 1\n            a,\
    \ b = line\n            p, q = self.data[k]\n            xl, xc, xr = self.X[l],\
    \ self.X[c], self.X[r - 1]\n            left = a * xl + b < p * xl + q\n     \
    \       center = a * xc + b < p * xc + q\n            right = a * xr + b < p *\
    \ xr + q\n\n            # update whole area with added line\n            if left\
    \ and right:\n                self.data[k] = line\n                return\n  \
    \          # no need to update\n            if not left and not right:\n     \
    \           return\n            # if more than half of segment is to be updated,\n\
    \            # swap newly added line and existing line.\n            if center:\n\
    \                self.data[k], line = line, self.data[k]\n            # search\
    \ [l, c)\n            if left != center:\n                r = c\n            \
    \    k = k << 1\n            # search [c, r)\n            else:\n            \
    \    l = c\n                k = k << 1 | 1\n"
  dependsOn: []
  isVerificationFile: false
  path: library/li_chao_tree.py
  requiredBy: []
  timestamp: '2023-04-17 16:54:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/line_add_get_min.test.py
  - tests/yosupo/segment_add_get_min.test.py
documentation_of: library/li_chao_tree.py
layout: document
redirect_from:
- /library/library/li_chao_tree.py
- /library/library/li_chao_tree.py.html
title: library/li_chao_tree.py
---
