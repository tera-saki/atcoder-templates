---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/dsl_3_d.test.py
    title: tests/aoj/dsl_3_d.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://scrapbox.io/data-structures/Sliding_Window_Aggregation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SWAG:\n    # reference: https://scrapbox.io/data-structures/Sliding_Window_Aggregation\n\
    \    def __init__(self, op):\n        self.op = op\n        self.front = []\n\
    \        self.back = []\n\n    def push(self, a):\n        if not self.back:\n\
    \            self.back.append((a, a))\n        else:\n            _, acc = self.back[-1]\n\
    \            self.back.append((a, self.op(acc, a)))\n\n    def pop(self):\n  \
    \      assert self.front or self.back\n        if not self.front:\n          \
    \  a, _ = self.back.pop()\n            self.front.append((a, a))\n           \
    \ while self.back:\n                a, _ = self.back.pop()\n                _,\
    \ acc = self.front[-1]\n                self.front.append((a, self.op(a, acc)))\n\
    \        self.front.pop()\n\n    def fold(self):\n        assert self.front or\
    \ self.back\n        if not self.front:\n            return self.back[-1][1]\n\
    \        if not self.back:\n            return self.front[-1][1]\n        return\
    \ self.op(self.front[-1][1], self.back[-1][1])\n"
  dependsOn: []
  isVerificationFile: false
  path: library/swag.py
  requiredBy: []
  timestamp: '2023-01-06 19:38:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/dsl_3_d.test.py
documentation_of: library/swag.py
layout: document
redirect_from:
- /library/library/swag.py
- /library/library/swag.py.html
title: library/swag.py
---
