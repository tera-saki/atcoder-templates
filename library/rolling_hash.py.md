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
  code: "import random\n\n\nclass RollingHash:\n    def __init__(self, S, mod=None,\
    \ base=None):\n        self.h = [0] * (len(S) + 1)\n        self.p = [1] * (len(S)\
    \ + 1)\n\n        if mod is None:\n            self.mod = (1 << 61) - 1\n    \
    \    else:\n            self.mod = mod\n\n        if base is None:\n         \
    \   self.base = random.randint(100, self.mod - 1)\n        else:\n           \
    \ self.base = base\n\n        for i in range(len(S)):\n            self.h[i +\
    \ 1] = (self.h[i] * self.base + ord(S[i])) % self.mod\n        for i in range(len(S)):\n\
    \            self.p[i + 1] = self.p[i] * self.base % self.mod\n\n    # S[l:r]\n\
    \    def get(self, l, r):\n        return (self.h[r] - self.h[l] * self.p[r -\
    \ l]) % self.mod\n"
  dependsOn: []
  isVerificationFile: false
  path: library/rolling_hash.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/rolling_hash.py
layout: document
redirect_from:
- /library/library/rolling_hash.py
- /library/library/rolling_hash.py.html
title: library/rolling_hash.py
---
