---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/bipartite_matching.py
    title: library/bipartite_matching.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartitematching
    links:
    - https://judge.yosupo.jp/problem/bipartitematching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching\n\
    import sys\nfrom library.bipartite_matching import BipartiteMatching\n\ninput\
    \ = sys.stdin.readline\n\nL, R, M = map(int, input().split())\nsolver = BipartiteMatching(L,\
    \ R)\nfor _ in range(M):\n    a, b = map(int, input().split())\n    solver.add_edge(a,\
    \ b)\nmatch = solver.solve()\nprint(match)\npairs = solver.pairs()\nfor l, r in\
    \ pairs:\n    print(l, r)\n"
  dependsOn:
  - library/bipartite_matching.py
  isVerificationFile: true
  path: tests/yosupo/bipartite_matching.test.py
  requiredBy: []
  timestamp: '2023-04-17 16:54:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/bipartite_matching.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/bipartite_matching.test.py
- /verify/tests/yosupo/bipartite_matching.test.py.html
title: tests/yosupo/bipartite_matching.test.py
---
