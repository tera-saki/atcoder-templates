---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/dsl_1_b.test.py
    title: tests/aoj/dsl_1_b.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class WeightedUnionFind:\n    def __init__(self, N):\n        self.N = N\n\
    \        self.par = [-1] * N\n        self.weight = [0] * N\n\n    def find(self,\
    \ x):\n        if self.par[x] < 0:\n            return x\n        p = self.find(self.par[x])\n\
    \        self.weight[x] += self.weight[self.par[x]]\n        self.par[x] = p\n\
    \        return self.par[x]\n\n    def merge(self, x, y, z):\n        \"Wy = Wx\
    \ + z\"\n        x_, y_ = x, y\n        x = self.find(x)\n        y = self.find(y)\n\
    \        wx = self.weight[x_]\n        wy = self.weight[y_]\n\n        if x ==\
    \ y:\n            return False\n        if self.par[x] > self.par[y]:\n      \
    \      x, y = y, x\n            wx, wy = wy, wx\n            z = -z\n\n      \
    \  self.par[x] += self.par[y]\n        self.par[y] = x\n        self.weight[y]\
    \ = z + wx - wy\n        return True\n\n    def diff(self, x, y):\n        \"\
    return Wy - Wx if calculable otherwise None\"\n        if self.find(x) != self.find(y):\n\
    \            return None\n        return self.weight[y] - self.weight[x]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/weighted_union_find.py
  requiredBy: []
  timestamp: '2022-12-12 21:09:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/dsl_1_b.test.py
documentation_of: library/weighted_union_find.py
layout: document
redirect_from:
- /library/library/weighted_union_find.py
- /library/library/weighted_union_find.py.html
title: library/weighted_union_find.py
---
