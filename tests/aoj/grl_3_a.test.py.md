---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/lowlink.py
    title: library/lowlink.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A\n\
    import sys\nfrom library.lowlink import Lowlink\n\ninput = sys.stdin.readline\n\
    \nN, M = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in range(M):\n\
    \    s, t = map(int, input().split())\n    E[s].append(t)\n    E[t].append(s)\n\
    \npoints = Lowlink(N, E).articulation_points()\nfor p in points:\n    print(p)\n"
  dependsOn:
  - library/lowlink.py
  isVerificationFile: true
  path: tests/aoj/grl_3_a.test.py
  requiredBy: []
  timestamp: '2022-12-14 18:34:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_3_a.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_3_a.test.py
- /verify/tests/aoj/grl_3_a.test.py.html
title: tests/aoj/grl_3_a.test.py
---
