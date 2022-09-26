---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: library/union_find.py
    title: library/union_find.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    import sys\nfrom library.union_find import UnionFind\n\ninput = sys.stdin.readline\n\
    \nN, Q = map(int, input().split())\nuf = UnionFind(N)\nfor _ in range(Q):\n  \
    \  t, u, v = map(int, input().split())\n    if t == 0:\n        uf.unite(u, v)\n\
    \    else:\n        print(1 if uf.same(u, v) else 0)\n"
  dependsOn:
  - library/union_find.py
  isVerificationFile: true
  path: tests/union_find.test.py
  requiredBy: []
  timestamp: '2022-09-26 23:57:29+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: tests/union_find.test.py
layout: document
redirect_from:
- /verify/tests/union_find.test.py
- /verify/tests/union_find.test.py.html
title: tests/union_find.test.py
---