---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/2871.test.py
    title: tests/aoj/2871.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class EulerTour:\n    def __init__(self, N, E, root=0):\n        self.N =\
    \ N\n        self.E = E\n        self.root = root\n        self.D = [0] * N\n\
    \        self.IN = [None] * N\n        self.OUT = [None] * N\n\n        self._traverse()\n\
    \n    def get_range(self, v):\n        return (self.IN[v], self.OUT[v])\n\n  \
    \  def _traverse(self):\n        stack = [(self.root, -1)]\n        cnt = 0\n\
    \        while stack:\n            v, p = stack.pop()\n            if v < 0:\n\
    \                self.OUT[~v] = cnt\n                cnt += 1\n              \
    \  continue\n\n            self.IN[v] = cnt\n            cnt += 1\n          \
    \  stack.append((~v, p))\n\n            if p >= 0:\n                self.D[v]\
    \ = self.D[p] + 1\n            for d in self.E[v][::-1]:\n                if d\
    \ == p:\n                    continue\n                stack.append((d, v))\n"
  dependsOn: []
  isVerificationFile: false
  path: library/euler_tour.py
  requiredBy: []
  timestamp: '2022-11-10 20:58:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/2871.test.py
documentation_of: library/euler_tour.py
layout: document
redirect_from:
- /library/library/euler_tour.py
- /library/library/euler_tour.py.html
title: library/euler_tour.py
---
