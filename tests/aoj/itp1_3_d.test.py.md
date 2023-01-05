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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ITP1_3_D\n\
    import sys\nfrom library.math import divisors\n\ninput = sys.stdin.readline\n\n\
    a, b, c = map(int, input().split())\ndivs = divisors(c)\nans = 0\nfor d in divs:\n\
    \    if a <= d <= b:\n        ans += 1\nprint(ans)\n"
  dependsOn:
  - library/math.py
  isVerificationFile: true
  path: tests/aoj/itp1_3_d.test.py
  requiredBy: []
  timestamp: '2023-01-05 19:39:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/itp1_3_d.test.py
layout: document
redirect_from:
- /verify/tests/aoj/itp1_3_d.test.py
- /verify/tests/aoj/itp1_3_d.test.py.html
title: tests/aoj/itp1_3_d.test.py
---
