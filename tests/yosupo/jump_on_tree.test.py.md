---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/lca.py
    title: library/lca.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/jump_on_tree
    links:
    - https://judge.yosupo.jp/problem/jump_on_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree\n\
    import sys\nfrom library.lca import LCA\n\ninput = sys.stdin.readline\n\nN, Q\
    \ = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in range(N -\
    \ 1):\n    a, b = map(int, input().split())\n    E[a].append(b)\n    E[b].append(a)\n\
    \nsolver = LCA(N, E)\nfor _ in range(Q):\n    s, t, i = map(int, input().split())\n\
    \    print(solver.jump(s, t, i))\n"
  dependsOn:
  - library/lca.py
  isVerificationFile: true
  path: tests/yosupo/jump_on_tree.test.py
  requiredBy: []
  timestamp: '2023-01-14 13:18:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/jump_on_tree.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/jump_on_tree.test.py
- /verify/tests/yosupo/jump_on_tree.test.py.html
title: tests/yosupo/jump_on_tree.test.py
---
