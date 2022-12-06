---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/swag.py
    title: library/swag.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D\n\
    import sys\nfrom library.swag import SWAG\n\ninput = sys.stdin.readline\n\nN,\
    \ L = map(int, input().split())\nA = list(map(int, input().split()))\n\nans =\
    \ []\nswag = SWAG(min)\nfor i in range(L):\n    swag.push(A[i])\nans.append(swag.fold())\n\
    \nfor i in range(L, N):\n    swag.pop()\n    swag.push(A[i])\n    ans.append(swag.fold())\n\
    \nprint(*ans)\n"
  dependsOn:
  - library/swag.py
  isVerificationFile: true
  path: tests/aoj/dsl_3_d.test.py
  requiredBy: []
  timestamp: '2022-12-06 18:49:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/dsl_3_d.test.py
layout: document
redirect_from:
- /verify/tests/aoj/dsl_3_d.test.py
- /verify/tests/aoj/dsl_3_d.test.py.html
title: tests/aoj/dsl_3_d.test.py
---
