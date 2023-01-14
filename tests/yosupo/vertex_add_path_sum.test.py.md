---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/binary_indexed_tree.py
    title: library/binary_indexed_tree.py
  - icon: ':heavy_check_mark:'
    path: library/hld.py
    title: library/hld.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    import sys\nfrom library.hld import HLD\nfrom library.binary_indexed_tree import\
    \ BIT\n\ninput = sys.stdin.readline\n\n\nN, Q = map(int, input().split())\nA =\
    \ list(map(int, input().split()))\nE = [[] for _ in range(N)]\nfor _ in range(N\
    \ - 1):\n    u, v = map(int, input().split())\n    E[u].append(v)\n    E[v].append(u)\n\
    \nsolver = HLD(N, E)\nB = [None] * N\nfor i, a in enumerate(A):\n    B[solver.ord[i]]\
    \ = a\nbit = BIT(N)\nbit.build(B)\nans = []\nfor _ in range(Q):\n    t, *q = map(int,\
    \ input().split())\n    if t == 0:\n        p, x = q\n        bit.add(solver.ord[p],\
    \ x)\n    else:\n        u, v = q\n        a = 0\n        for l, r in solver.path_query_range(u,\
    \ v):\n            a += bit.range_sum(l, r)\n        ans.append(a)\nprint(*ans,\
    \ sep='\\n')\n"
  dependsOn:
  - library/hld.py
  - library/binary_indexed_tree.py
  isVerificationFile: true
  path: tests/yosupo/vertex_add_path_sum.test.py
  requiredBy: []
  timestamp: '2023-01-14 13:08:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/vertex_add_path_sum.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/vertex_add_path_sum.test.py
- /verify/tests/yosupo/vertex_add_path_sum.test.py.html
title: tests/yosupo/vertex_add_path_sum.test.py
---
