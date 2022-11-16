---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yuki/1006.test.py
    title: tests/yuki/1006.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Osa_k:\n    # N\u4EE5\u4E0B\u306E\u6574\u6570\u3092\u7D20\u56E0\u6570\
    \u5206\u89E3 O(NlogN)\n    def __init__(self, N):\n        self.min_factor = [i\
    \ for i in range(N + 1)]\n        for i in range(2, N + 1):\n            if i\
    \ * i > N:\n                break\n            if self.min_factor[i] == i:\n \
    \               for j in range(2, N + 1):\n                    if i * j > N:\n\
    \                        break\n                    if self.min_factor[i * j]\
    \ > i:\n                        self.min_factor[i * j] = i\n\n    def factors(self,\
    \ n):\n        f = []\n        while n > 1:\n            f.append(self.min_factor[n])\n\
    \            n //= self.min_factor[n]\n        return f\n"
  dependsOn: []
  isVerificationFile: false
  path: library/osa_k.py
  requiredBy: []
  timestamp: '2022-11-16 21:30:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yuki/1006.test.py
documentation_of: library/osa_k.py
layout: document
redirect_from:
- /library/library/osa_k.py
- /library/library/osa_k.py.html
title: library/osa_k.py
---
