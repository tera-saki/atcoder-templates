---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/0549.test.py
    title: tests/aoj/0549.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class CumulativeSum:\n    def __init__(self, A):\n        self.S = [0]\n\
    \        acc = 0\n        for a in A:\n            acc += a\n            self.S.append(acc)\n\
    \n    def get(self, l, r):\n        \"\"\"return sum(A[l:r]), i.e. sum of A[x]\
    \ (l <= x < r) \"\"\"\n        return self.S[r] - self.S[l]\n"
  dependsOn: []
  isVerificationFile: false
  path: library/cumulative_sum.py
  requiredBy: []
  timestamp: '2022-12-06 18:26:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/0549.test.py
documentation_of: library/cumulative_sum.py
layout: document
redirect_from:
- /library/library/cumulative_sum.py
- /library/library/cumulative_sum.py.html
title: library/cumulative_sum.py
---
