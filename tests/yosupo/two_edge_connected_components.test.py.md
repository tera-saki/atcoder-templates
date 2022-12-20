---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/dfs_tree.py
    title: library/dfs_tree.py
  - icon: ':heavy_check_mark:'
    path: library/union_find.py
    title: library/union_find.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_edge_connected_components
    links:
    - https://judge.yosupo.jp/problem/two_edge_connected_components
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components\n\
    import sys\nfrom collections import defaultdict\nfrom library.dfs_tree import\
    \ DFSTree\nfrom library.union_find import UnionFind\n\ninput = sys.stdin.readline\n\
    \nN, M = map(int, input().split())\nE = [[] for _ in range(N)]\nedges = [tuple(map(int,\
    \ input().split())) for _ in range(M)]\nedges = [(u, v) if u < v else (v, u) for\
    \ u, v in edges]\ncnt = defaultdict(int)\nfor a, b in edges:\n    E[a].append(b)\n\
    \    E[b].append(a)\n    cnt[(a, b)] += 1\ndups = set((a, b) for (a, b) in edges\
    \ if cnt[(a, b)] > 1)\n\nbridges = DFSTree(N, E).bridges()\nB = set((u, v) if\
    \ u < v else (v, u) for u, v in bridges)\nfor u, v in dups:\n    B.discard((u,\
    \ v))\nuf = UnionFind(N)\nfor u, v in edges:\n    if (u, v) in B:\n        continue\n\
    \    uf.unite(u, v)\n\ngroups = [[] for _ in range(N)]\nfor i in range(N):\n \
    \   par = uf.find(i)\n    groups[par].append(i)\ngroups = [g for g in groups if\
    \ g]\nprint(len(groups))\nfor g in groups:\n    print(len(g), *g)\n"
  dependsOn:
  - library/dfs_tree.py
  - library/union_find.py
  isVerificationFile: true
  path: tests/yosupo/two_edge_connected_components.test.py
  requiredBy: []
  timestamp: '2022-12-20 01:37:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/two_edge_connected_components.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/two_edge_connected_components.test.py
- /verify/tests/yosupo/two_edge_connected_components.test.py.html
title: tests/yosupo/two_edge_connected_components.test.py
---
