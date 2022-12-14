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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B\n\
    import sys\nfrom library.lowlink import Lowlink\n\ninput = sys.stdin.readline\n\
    \nN, M = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in range(M):\n\
    \    s, t = map(int, input().split())\n    E[s].append(t)\n    E[t].append(s)\n\
    \nbridges = Lowlink(N, E).bridges()\nbridges = [(s, t) if s < t else (t, s) for\
    \ s, t in bridges]\nfor s, t in sorted(bridges):\n    print(s, t)\n"
  dependsOn:
  - library/lowlink.py
  isVerificationFile: true
  path: tests/aoj/grl_3_b.test.py
  requiredBy: []
  timestamp: '2022-12-14 18:34:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_3_b.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_3_b.test.py
- /verify/tests/aoj/grl_3_b.test.py.html
title: tests/aoj/grl_3_b.test.py
---
