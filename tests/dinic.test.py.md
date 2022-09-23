---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/dinic.py
    title: library/dinic.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A\n\
    import sys\nfrom library.dinic import Dinic\n\ninput = sys.stdin.readline\n\n\
    N, M = map(int, input().split())\ndinic = Dinic(N)\nfor _ in range(M):\n    u,\
    \ v, cap = map(int, input().split())\n    dinic.add_edge(u, v, cap)\nprint(dinic.flow(0,\
    \ N - 1))\n"
  dependsOn:
  - library/dinic.py
  isVerificationFile: true
  path: tests/dinic.test.py
  requiredBy: []
  timestamp: '2022-09-23 21:22:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/dinic.test.py
layout: document
redirect_from:
- /verify/tests/dinic.test.py
- /verify/tests/dinic.test.py.html
title: tests/dinic.test.py
---
