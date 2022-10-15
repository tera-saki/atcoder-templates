---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/dijkstra.py
    title: library/dijkstra.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    import sys\nfrom library.dijkstra import Dijkstra\n\ninput = sys.stdin.readline\n\
    \nN, M, s, t = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in\
    \ range(M):\n    a, b, c = map(int, input().split())\n    E[a].append((c, b))\n\
    \nsolver = Dijkstra(N, E, start=s)\ncost = solver.get_cost(t)\nif cost is None:\n\
    \    print(-1)\n    exit()\np = solver.get_path(t)\nprint(cost, len(p) - 1)\n\
    for a, b in zip(p[:-1], p[1:]):\n    print(a, b)\n"
  dependsOn:
  - library/dijkstra.py
  isVerificationFile: true
  path: tests/yosupo/shortest_path.test.py
  requiredBy: []
  timestamp: '2022-10-15 16:47:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/shortest_path.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/shortest_path.test.py
- /verify/tests/yosupo/shortest_path.test.py.html
title: tests/yosupo/shortest_path.test.py
---
