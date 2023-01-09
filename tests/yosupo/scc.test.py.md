---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/scc.py
    title: library/scc.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/scc
    links:
    - https://judge.yosupo.jp/problem/scc
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc\nimport\
    \ sys\nfrom library.scc import SCC\n\ninput = sys.stdin.readline\nsys.setrecursionlimit(10\
    \ ** 6)\n\nN, M = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _\
    \ in range(M):\n    a, b = map(int, input().split())\n    E[a].append(b)\nscc\
    \ = SCC(N, E)\n\nprint(scc.c_num)\nfor i in range(scc.c_num):\n    print(len(scc.C[i]),\
    \ *scc.C[i])\n"
  dependsOn:
  - library/scc.py
  isVerificationFile: true
  path: tests/yosupo/scc.test.py
  requiredBy: []
  timestamp: '2023-01-09 20:43:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/scc.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/scc.test.py
- /verify/tests/yosupo/scc.test.py.html
title: tests/yosupo/scc.test.py
---
