---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/lis.py
    title: library/lis.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/DPL_1_D

    import sys

    from library.lis import LIS


    input = sys.stdin.readline



    N = int(input())

    A = [int(input()) for _ in range(N)]

    print(LIS(A).solve())

    '
  dependsOn:
  - library/lis.py
  isVerificationFile: true
  path: tests/lis.test.py
  requiredBy: []
  timestamp: '2022-09-27 01:14:22+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/lis.test.py
layout: document
redirect_from:
- /verify/tests/lis.test.py
- /verify/tests/lis.test.py.html
title: tests/lis.test.py
---
