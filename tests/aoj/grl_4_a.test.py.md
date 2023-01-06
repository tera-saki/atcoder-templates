---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/topological_sort.py
    title: library/topological_sort.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A\n\
    import sys\nfrom library.topological_sort import TopologicalSort\n\ninput = sys.stdin.readline\n\
    N, M = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in range(M):\n\
    \    a, b = map(int, input().split())\n    E[a].append(b)\n\nprint(0 if TopologicalSort(N,\
    \ E).sort() else 1)\n"
  dependsOn:
  - library/topological_sort.py
  isVerificationFile: true
  path: tests/aoj/grl_4_a.test.py
  requiredBy: []
  timestamp: '2023-01-07 00:50:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_4_a.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_4_a.test.py
- /verify/tests/aoj/grl_4_a.test.py.html
title: tests/aoj/grl_4_a.test.py
---
