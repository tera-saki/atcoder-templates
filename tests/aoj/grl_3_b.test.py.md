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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B\n\
    import sys\nfrom library.dfs_tree import DFSTree\n\ninput = sys.stdin.readline\n\
    \nN, M = map(int, input().split())\ndfs_tree = DFSTree(N)\nfor _ in range(M):\n\
    \    s, t = map(int, input().split())\n    dfs_tree.add_edge(s, t)\ndfs_tree.build()\n\
    bridges = dfs_tree.bridges()\nbridges = [(s, t) if s < t else (t, s) for s, t\
    \ in bridges]\nfor s, t in sorted(bridges):\n    print(s, t)\n"
  dependsOn:
  - library/dfs_tree.py
  isVerificationFile: true
  path: tests/aoj/grl_3_b.test.py
  requiredBy: []
  timestamp: '2023-01-09 18:15:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/aoj/grl_3_b.test.py
layout: document
redirect_from:
- /verify/tests/aoj/grl_3_b.test.py
- /verify/tests/aoj/grl_3_b.test.py.html
title: tests/aoj/grl_3_b.test.py
---
