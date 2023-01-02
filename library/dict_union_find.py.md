---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import defaultdict\n\n\nclass UnionFindDict:\n    def __init__(self):\n\
    \        self.par = defaultdict(lambda: -1)\n\n    def find(self, x):\n      \
    \  if self.par[x] < 0:\n            return x\n        else:\n            self.par[x]\
    \ = self.find(self.par[x])\n            return self.par[x]\n\n    def unite(self,\
    \ x, y):\n        x = self.find(x)\n        y = self.find(y)\n\n        if x ==\
    \ y:\n            return False\n        if self.par[x] > self.par[y]:\n      \
    \      x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n        return True\n\n    def same(self, x, y):\n        return self.find(x)\
    \ == self.find(y)\n\n    def size(self, x):\n        return -self.par[self.find(x)]\n\
    \n    def roots(self):\n        return [k for k, v in self.par.items() if v <\
    \ 0]\n\n    def members(self, x):\n        p = self.find(x)\n        return [k\
    \ for k in self.par if self.find(k) == p]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/dict_union_find.py
  requiredBy: []
  timestamp: '2023-01-02 14:29:55+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/dict_union_find.py
layout: document
redirect_from:
- /library/library/dict_union_find.py
- /library/library/dict_union_find.py.html
title: library/dict_union_find.py
---
