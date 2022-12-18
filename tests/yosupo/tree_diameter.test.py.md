---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/tree_diameter.py
    title: library/tree_diameter.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/tree_diameter
    links:
    - https://judge.yosupo.jp/problem/tree_diameter
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter\n\
    import sys\nfrom library.tree_diameter import TreeDiameter\n\ninput = sys.stdin.readline\n\
    \nN = int(input())\nE = [[] for _ in range(N)]\nfor _ in range(N - 1):\n    a,\
    \ b, c = map(int, input().split())\n    E[a].append((c, b))\n    E[b].append((c,\
    \ a))\nsolver = TreeDiameter(N, E)\npath = solver.get_path()\nprint(solver.diameter_weight,\
    \ len(path))\nprint(*solver.get_path())\n"
  dependsOn:
  - library/tree_diameter.py
  isVerificationFile: true
  path: tests/yosupo/tree_diameter.test.py
  requiredBy: []
  timestamp: '2022-12-18 14:07:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/tree_diameter.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/tree_diameter.test.py
- /verify/tests/yosupo/tree_diameter.test.py.html
title: tests/yosupo/tree_diameter.test.py
---
