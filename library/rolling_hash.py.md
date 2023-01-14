---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/alds1_14_b.test.py
    title: tests/aoj/alds1_14_b.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\n\n\nclass RollingHash:\n    # reference: https://qiita.com/keymoon/items/11fac5627672a6d6a9f6\n\
    \    MSK30 = (1 << 30) - 1\n    MSK31 = (1 << 31) - 1\n    MOD = (1 << 61) - 1\n\
    \    MSK61 = MOD\n\n    def __init__(self, S, base=None):\n        self.h = [0]\
    \ * (len(S) + 1)\n        self.p = [1] * (len(S) + 1)\n\n        if base is None:\n\
    \            self.base = random.randint(2, self.MOD - 2)\n        else:\n    \
    \        self.base = base\n\n        for i in range(len(S)):\n            self.h[i\
    \ + 1] = self._mod(self._mul(self.h[i], self.base) + ord(S[i]))\n        for i\
    \ in range(len(S)):\n            self.p[i + 1] = self._mul(self.p[i], self.base)\n\
    \n    # S[l:r]\n    def get(self, l, r):\n        \"\"\"return hash of S[l:r]\"\
    \"\"\n        return self._mod(self.h[r] - self._mul(self.h[l], self.p[r - l]))\n\
    \n    def merge(self, l1, r1, l2, r2):\n        \"\"\"return hash of S[l1:r1]\
    \ + S[l2:r2]\"\"\"\n        h1 = self.get(l1, r1)\n        h2 = self.get(l2, r2)\n\
    \        return self._mod(self._mul(h1, self.p[r2 - l2]) + h2)\n\n    def _mul(self,\
    \ a, b):\n        au, ad = a >> 31, a & self.MSK31\n        bu, bd = b >> 31,\
    \ b & self.MSK31\n        mid = ad * bu + au * bd\n        midu, midd = mid >>\
    \ 30, mid & self.MSK30\n        return self._mod(au * bu * 2 + midu + (midd <<\
    \ 31) + ad * bd)\n\n    def _mod(self, x):\n        xu, xd = x >> 61, x & self.MSK61\n\
    \        ret = xu + xd\n        if ret >= self.MOD:\n            ret -= self.MOD\n\
    \        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: library/rolling_hash.py
  requiredBy: []
  timestamp: '2023-01-14 16:20:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/alds1_14_b.test.py
documentation_of: library/rolling_hash.py
layout: document
redirect_from:
- /library/library/rolling_hash.py
- /library/library/rolling_hash.py.html
title: library/rolling_hash.py
---
