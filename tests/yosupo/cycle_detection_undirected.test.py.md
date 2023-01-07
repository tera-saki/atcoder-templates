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
    \n\nN, M = map(int, input().split())\ndfs_tree = DFSTree(N)\nfor i in range(M):\n\
    \    u, v = map(int, input().split())\n    dfs_tree.add_edge(u, v)\ndfs_tree.build()\n\
    \nfor i in range(N):\n    if not dfs_tree.back_edge[i]:\n        continue\n  \
    \  backto, eidx = dfs_tree.back_edge[i][0]\n    V = [backto]\n    E = [eidx]\n\
    \    cur = i\n    while True:\n        if cur == backto:\n            break\n\
    \        v, eidx = dfs_tree.par[cur]\n        V.append(cur)\n        E.append(eidx)\n\
    \        cur = v\n    print(len(V))\n    print(*V)\n    print(*E)\n    break\n\
    else:\n    print(-1)\n"
  dependsOn:
  - library/dfs_tree.py
  isVerificationFile: true
  path: tests/yosupo/cycle_detection_undirected.test.py
  requiredBy: []
  timestamp: '2023-01-07 12:45:37+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/cycle_detection_undirected.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/cycle_detection_undirected.test.py
- /verify/tests/yosupo/cycle_detection_undirected.test.py.html
title: tests/yosupo/cycle_detection_undirected.test.py
---
