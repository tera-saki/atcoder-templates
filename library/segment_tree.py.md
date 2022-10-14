---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/point_add_range_sum.test.py
    title: tests/yosupo/point_add_range_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegTree:\n    def __init__(self, N, func, e):\n        self.N = N\n\
    \        self.func = func\n        self.X = [e] * (N << 1)\n        self.e = e\n\
    \n    def build(self, seq):\n        for i in range(self.N):\n            self.X[self.N\
    \ + i] = seq[i]\n        for i in range(self.N)[::-1]:\n            self.X[i]\
    \ = self.func(self.X[i << 1], self.X[i << 1 | 1])\n\n    def add(self, i, x):\n\
    \        i += self.N\n        self.X[i] += x\n        while i > 1:\n         \
    \   i >>= 1\n            self.X[i] = self.func(self.X[i << 1], self.X[i << 1 |\
    \ 1])\n\n    def update(self, i, x):\n        i += self.N\n        self.X[i] =\
    \ x\n        while i > 1:\n            i >>= 1\n            self.X[i] = self.func(self.X[i\
    \ << 1], self.X[i << 1 | 1])\n\n    def query(self, L, R):\n        L += self.N\n\
    \        R += self.N\n        vL = self.e\n        vR = self.e\n        while\
    \ L < R:\n            if L & 1:\n                vL = self.func(vL, self.X[L])\n\
    \                L += 1\n            if R & 1:\n                R -= 1\n     \
    \           vR = self.func(self.X[R], vR)\n            L >>= 1\n            R\
    \ >>= 1\n        return self.func(vL, vR)\n"
  dependsOn: []
  isVerificationFile: false
  path: library/segment_tree.py
  requiredBy: []
  timestamp: '2022-10-14 23:33:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/point_add_range_sum.test.py
documentation_of: library/segment_tree.py
layout: document
redirect_from:
- /library/library/segment_tree.py
- /library/library/segment_tree.py.html
title: library/segment_tree.py
---
