---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/zalgorithm.test.py
    title: tests/yosupo/zalgorithm.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Z_Algorhthm:\n    \"\"\"calculate Z[i] := longest common prefix of\
    \ S and S[i:]\n    reference: https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05\n\
    \    \"\"\"\n\n    def __init__(self, S):\n        self.Z = [None] * len(S)\n\n\
    \        self.Z[0] = len(S)\n        i, j = 1, 0\n        while i < len(S):\n\
    \            while i + j < len(S) and S[j] == S[i + j]:\n                j +=\
    \ 1\n            self.Z[i] = j\n\n            if j == 0:\n                i +=\
    \ 1\n                continue\n\n            k = 1\n            while k < j and\
    \ k + self.Z[k] < j:\n                self.Z[i + k] = self.Z[k]\n            \
    \    k += 1\n            i += k\n            j -= k\n"
  dependsOn: []
  isVerificationFile: false
  path: library/string.py
  requiredBy: []
  timestamp: '2023-01-09 18:15:55+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/yosupo/zalgorithm.test.py
documentation_of: library/string.py
layout: document
redirect_from:
- /library/library/string.py
- /library/library/string.py.html
title: library/string.py
---
