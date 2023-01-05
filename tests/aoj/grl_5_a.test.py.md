---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/rerooting.py
    title: library/rerooting.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A\n\
    import sys\nfrom library.rerooting import Rerooting\n\ninput = sys.stdin.readline\n\
    \nN = int(input())\nE = [[] for _ in range(N)]\nfor _ in range(N - 1):\n    s,\
    \ t, w = map(int, input().split())\n    E[s].append((w, t))\n    E[t].append((w,\
    \ s))\n\n\ndef f(a, v, ch, cost):\n    return a + cost\n\n\ndef g(a, v):\n   \
    \ return a\n\n\ndef merge(a, b):\n    return max(a, b)\n\n\nsolver = Rerooting(N,\
    \ E, f, g, merge, 0)\nans = 0\nfor i in range(N):\n    v = solver.solve(i)\n \
    \   ans = max(ans, v)\nprint(ans)\n"
  dependsOn:
  - library/rerooting.py
  isVerificationFile: true
  path: tests/aoj/grl_5_a.test.py
  requiredBy: []
  timestamp: '2023-01-05 18:27:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_5_a.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_5_a.test.py
- /verify/tests/aoj/grl_5_a.test.py.html
title: tests/aoj/grl_5_a.test.py
---
