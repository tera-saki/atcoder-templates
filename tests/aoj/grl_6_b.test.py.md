---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/primal_dual.py
    title: library/primal_dual.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B\n\
    import sys\nfrom library.primal_dual import PrimalDual\n\ninput = sys.stdin.readline\n\
    \nN, M, F = map(int, input().split())\nsolver = PrimalDual(N)\nfor _ in range(M):\n\
    \    u, v, cap, cost = map(int, input().split())\n    solver.add_edge(u, v, cap,\
    \ cost)\nf, c = solver.flow(0, N - 1, F)\nprint(c if f == F else -1)\n"
  dependsOn:
  - library/primal_dual.py
  isVerificationFile: true
  path: tests/aoj/grl_6_b.test.py
  requiredBy: []
  timestamp: '2023-01-06 21:27:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_6_b.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_6_b.test.py
- /verify/tests/aoj/grl_6_b.test.py.html
title: tests/aoj/grl_6_b.test.py
---
