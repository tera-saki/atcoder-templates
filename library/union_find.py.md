---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/union_find.test.py
    title: tests/yosupo/union_find.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, N):\n        self.N = N\n      \
    \  self.par = [-1] * N\n\n    def find(self, x):\n        if self.par[x] < 0:\n\
    \            return x\n        else:\n            self.par[x] = self.find(self.par[x])\n\
    \            return self.par[x]\n\n    def unite(self, x, y):\n        x = self.find(x)\n\
    \        y = self.find(y)\n\n        if x == y:\n            return False\n  \
    \      if self.par[x] > self.par[y]:\n            x, y = y, x\n\n        self.par[x]\
    \ += self.par[y]\n        self.par[y] = x\n        return True\n\n    def same(self,\
    \ x, y):\n        return self.find(x) == self.find(y)\n\n    def size(self, x):\n\
    \        return -self.par[self.find(x)]\n\n    def roots(self):\n        return\
    \ [i for i in range(self.N) if self.par[i] < 0]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/union_find.py
  requiredBy: []
  timestamp: '2022-12-18 13:51:57+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/union_find.test.py
documentation_of: library/union_find.py
layout: document
redirect_from:
- /library/library/union_find.py
- /library/library/union_find.py.html
title: library/union_find.py
---
