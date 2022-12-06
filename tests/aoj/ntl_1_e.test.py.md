---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/math.py
    title: library/math.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E

    import sys

    from library.math import extgcd


    input = sys.stdin.readline


    a, b = map(int, input().split())

    _, x, y = extgcd(a, b)

    print(x, y)

    '
  dependsOn:
  - library/math.py
  isVerificationFile: true
  path: tests/aoj/ntl_1_e.test.py
  requiredBy: []
  timestamp: '2022-12-06 18:26:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/ntl_1_e.test.py
layout: document
redirect_from:
- /verify/tests/aoj/ntl_1_e.test.py
- /verify/tests/aoj/ntl_1_e.test.py.html
title: tests/aoj/ntl_1_e.test.py
---
