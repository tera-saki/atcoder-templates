---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://atcoder.jp/contests/abc259/tasks/abc259_c
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\ninput = sys.stdin.readline\n\n\nclass RLE:\n    @classmethod\n\
    \    def encode(self, S):\n        A = [[S[0], 1]]\n        for i in range(1,\
    \ len(S)):\n            if S[i] != S[i - 1]:\n                A.append([S[i],\
    \ 1])\n            else:\n                A[-1][1] += 1\n        return [tuple(p)\
    \ for p in A]\n\n\n# https://atcoder.jp/contests/abc259/tasks/abc259_c\nS = input()[:-1]\n\
    T = input()[:-1]\n\nSe = RLE.encode(S)\nTe = RLE.encode(T)\n\nif len(Se) != len(Te):\n\
    \    print('No')\n    exit()\n\nfor (s, n), (t, m) in zip(Se, Te):\n    if s !=\
    \ t or n > m:\n        print('No')\n        exit()\n    if n == 1 and m > 1:\n\
    \        print('No')\n        exit()\nprint('Yes')\n"
  dependsOn: []
  isVerificationFile: false
  path: library/rle.py
  requiredBy: []
  timestamp: '2022-09-29 01:54:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: library/rle.py
layout: document
redirect_from:
- /library/library/rle.py
- /library/library/rle.py.html
title: library/rle.py
---
