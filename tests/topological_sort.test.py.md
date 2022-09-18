---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: ''
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_B
    - https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/GRL_4_B/judge/6940421/Python3
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_B\n\
    # verification-helper: IGNORE\n# https://onlinejudge.u-aizu.ac.jp/status/users/terasa/submissions/1/GRL_4_B/judge/6940421/Python3\n\
    import sys\nfrom library.topological_sort import TopologicalSort\n\ninput = sys.stdin.readline\n\
    \nN, M = map(int, input().split())\nE = [[] for _ in range(N)]\nfor _ in range(M):\n\
    \    a, b = map(int, input().split())\n    E[a].append(b)\n\nret = TopologicalSort(N,\
    \ E).sort()\nprint(*ret, sep='\\n')\n"
  dependsOn: []
  isVerificationFile: true
  path: tests/topological_sort.test.py
  requiredBy: []
  timestamp: '2022-09-18 21:34:34+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: tests/topological_sort.test.py
layout: document
redirect_from:
- /verify/tests/topological_sort.test.py
- /verify/tests/topological_sort.test.py.html
title: tests/topological_sort.test.py
---
