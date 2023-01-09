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
    PROBLEM: https://judge.yosupo.jp/problem/biconnected_components
    links:
    - https://judge.yosupo.jp/problem/biconnected_components
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/biconnected_components\n\
    import sys\nfrom library.dfs_tree import DFSTree\n\ninput = sys.stdin.readline\n\
    \nN, M = map(int, input().split())\ndfs_tree = DFSTree(N)\nfor _ in range(M):\n\
    \    a, b = map(int, input().split())\n    dfs_tree.add_edge(a, b)\ndfs_tree.build()\n\
    B = dfs_tree.biconnected_components()\nprint(len(B))\nfor bcc in B:\n    print(len(bcc),\
    \ *bcc)\n"
  dependsOn:
  - library/dfs_tree.py
  isVerificationFile: true
  path: tests/yosupo/biconnected_components.test.py
  requiredBy: []
  timestamp: '2023-01-09 20:43:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/biconnected_components.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/biconnected_components.test.py
- /verify/tests/yosupo/biconnected_components.test.py.html
title: tests/yosupo/biconnected_components.test.py
---
