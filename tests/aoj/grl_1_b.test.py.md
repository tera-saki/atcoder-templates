---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/bellman_ford.py
    title: library/bellman_ford.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B\n\
    import sys\nfrom library.bellman_ford import BellmanFord\n\ninput = sys.stdin.readline\n\
    \nN, M, start = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in\
    \ range(M):\n    s, t, d = map(int, input().split())\n    E[s].append((d, t))\n\
    \nsolver = BellmanFord(N, E, start=start)\ncost = [solver.get_cost(i) for i in\
    \ range(N)]\nans = []\nfor c in cost:\n    if c == -solver.inf:\n        print('NEGATIVE\
    \ CYCLE')\n        exit()\n    ans.append(c if c < solver.inf else 'INF')\nprint(*ans,\
    \ sep='\\n')\n"
  dependsOn:
  - library/bellman_ford.py
  isVerificationFile: true
  path: tests/aoj/grl_1_b.test.py
  requiredBy: []
  timestamp: '2022-12-18 14:07:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_1_b.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_1_b.test.py
- /verify/tests/aoj/grl_1_b.test.py.html
title: tests/aoj/grl_1_b.test.py
---
