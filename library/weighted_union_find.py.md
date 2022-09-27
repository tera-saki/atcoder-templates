---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/weighted_union_find.test.py
    title: tests/weighted_union_find.test.py
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
    \ x, w=0):\n        if self.par[x] < 0:\n            return x, w\n        else:\n\
    \            return self.find(self.par[x], w + self.weight[x])\n\n    def merge(self,\
    \ x, y, z):\n        \"Wy = Wx + z\"\n        x, wx = self.find(x)\n        y,\
    \ wy = self.find(y)\n\n        if x == y:\n            return False\n        if\
    \ self.par[x] > self.par[y]:\n            x, y = y, x\n            wx, wy = wy,\
    \ wx\n            z = -z\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n        self.weight[y] = z + wx - wy\n        return True\n\n    def diff(self,\
    \ x, y):\n        \"return Wy - Wx if calculable otherwise None\"\n        x,\
    \ wx = self.find(x)\n        y, wy = self.find(y)\n\n        if x != y:\n    \
    \        return None\n        return wy - wx\n\n    def same(self, x, y):\n  \
    \      return self.find(x)[0] == self.find(y)[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/weighted_union_find.py
  requiredBy: []
  timestamp: '2022-09-27 20:48:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/weighted_union_find.test.py
documentation_of: library/weighted_union_find.py
layout: document
redirect_from:
- /library/library/weighted_union_find.py
- /library/library/weighted_union_find.py.html
title: library/weighted_union_find.py
---
