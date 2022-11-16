---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/bfs.py
    title: library/bfs.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_11_C\n\
    import sys\nfrom library.bfs import BFS\n\ninput = sys.stdin.readline\n\nN = int(input())\n\
    E = []\nfor _ in range(N):\n    u, k, *V = map(int, input().split())\n    E.append([v\
    \ - 1 for v in V])\n\nsolver = BFS(N, E)\nfor i in range(N):\n    c = solver.get_cost(i)\n\
    \    print(i + 1, c if c < solver.inf else -1)\n"
  dependsOn:
  - library/bfs.py
  isVerificationFile: true
  path: tests/aoj/alds1_11_c.test.py
  requiredBy: []
  timestamp: '2022-11-16 19:43:31+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/alds1_11_c.test.py
layout: document
redirect_from:
- /verify/tests/aoj/alds1_11_c.test.py
- /verify/tests/aoj/alds1_11_c.test.py.html
title: tests/aoj/alds1_11_c.test.py
---
