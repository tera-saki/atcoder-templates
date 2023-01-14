---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/doubling_lca.py
    title: library/doubling_lca.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/lca
    links:
    - https://judge.yosupo.jp/problem/lca
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca\nimport\
    \ sys\nfrom library.doubling_lca import LCA\n\ninput = sys.stdin.readline\n\n\
    N, Q = map(int, input().split())\nP = list(map(int, input().split()))\nE = [[]\
    \ for _ in range(N)]\nfor i, p in enumerate(P, start=1):\n    E[i].append(p)\n\
    \    E[p].append(i)\n\nsolver = LCA(N, E)\nfor _ in range(Q):\n    u, v = map(int,\
    \ input().split())\n    print(solver.lca(u, v))\n"
  dependsOn:
  - library/doubling_lca.py
  isVerificationFile: true
  path: tests/yosupo/lca-doubling.test.py
  requiredBy: []
  timestamp: '2023-01-14 22:09:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/lca-doubling.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/lca-doubling.test.py
- /verify/tests/yosupo/lca-doubling.test.py.html
title: tests/yosupo/lca-doubling.test.py
---
