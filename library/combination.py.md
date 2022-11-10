---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yuki/117.test.py
    title: tests/yuki/117.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Combination:\n    def __init__(self, N, mod):\n        self.N = N\n\
    \        self.mod = mod\n        self.f = [None] * (N + 1)\n        self.finv\
    \ = [None] * (N + 1)\n        self.inv = [None] * (N + 1)\n\n        self.f[0]\
    \ = 1\n        self.f[1] = 1\n        self.finv[0] = 1\n        self.finv[1] =\
    \ 1\n        self.inv[1] = 1\n        for i in range(2, N + 1):\n            self.f[i]\
    \ = self.f[i - 1] * i % self.mod\n            self.inv[i] = self.mod - self.inv[self.mod\
    \ % i] * (self.mod // i) % self.mod\n            self.finv[i] = self.finv[i -\
    \ 1] * self.inv[i] % self.mod\n\n    def P(self, n, k):\n        if n < k:\n \
    \           return 0\n        if n < 0 or k < 0:\n            return 0\n     \
    \   return self.f[n] * self.finv[n - k] % self.mod\n\n    def C(self, n, k):\n\
    \        if n < k:\n            return 0\n        if n < 0 or k < 0:\n       \
    \     return 0\n        return self.f[n] * (self.finv[k] * self.finv[n - k] %\
    \ self.mod) % self.mod\n\n    # \u91CD\u8907\u7D44\u5408\u305B\n    # n\u7A2E\u985E\
    \u306E\u3082\u306E\u304B\u3089k\u500B\u9078\u3076\n    def H(self, n, k):\n  \
    \      if n == 0 and k == 0:\n            return 1\n        return self.C(k +\
    \ n - 1, k)\n\n"
  dependsOn: []
  isVerificationFile: false
  path: library/combination.py
  requiredBy: []
  timestamp: '2022-11-10 20:58:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yuki/117.test.py
documentation_of: library/combination.py
layout: document
redirect_from:
- /library/library/combination.py
- /library/library/combination.py.html
title: library/combination.py
---
