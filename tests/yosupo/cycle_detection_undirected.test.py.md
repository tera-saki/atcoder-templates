---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/dfs_tree.py
    title: library/dfs_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/cycle_detection_undirected
    links:
    - https://judge.yosupo.jp/problem/cycle_detection_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected\n\
    import sys\nfrom library.dfs_tree import DFSTree\n\ninput = sys.stdin.readline\n\
    \n\nN, M = map(int, input().split())\nE = [[] for _ in range(N)]\neidx = {}\n\
    for i in range(M):\n    u, v = map(int, input().split())\n    E[u].append(v)\n\
    \    E[v].append(u)\n    if u > v:\n        u, v = v, u\n    j = eidx.get((u,\
    \ v))\n    if j is None:\n        eidx[(u, v)] = i\n    else:\n        print(2)\n\
    \        print(u, v)\n        print(i, j)\n        exit()\n\nsolver = DFSTree(N,\
    \ E)\nback_edges = solver.back_edge\nfor i in range(N):\n    if not back_edges[i]:\n\
    \        continue\n    backto = back_edges[i][0]\n    path = solver.get_path(i)\n\
    \    ansv = path[path.index(backto):]\n    anse = []\n    for s, t in zip(ansv,\
    \ ansv[1:]):\n        if s > t:\n            s, t = t, s\n        anse.append(eidx[(s,\
    \ t)])\n    anse.append(eidx[min(i, backto), max(i, backto)])\n    print(len(ansv))\n\
    \    print(*ansv)\n    print(*anse)\n    break\nelse:\n    print(-1)\n"
  dependsOn:
  - library/dfs_tree.py
  isVerificationFile: true
  path: tests/yosupo/cycle_detection_undirected.test.py
  requiredBy: []
  timestamp: '2022-12-14 19:31:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/cycle_detection_undirected.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/cycle_detection_undirected.test.py
- /verify/tests/yosupo/cycle_detection_undirected.test.py.html
title: tests/yosupo/cycle_detection_undirected.test.py
---
