---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/two_sat.py
    title: library/two_sat.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_sat
    links:
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat\n\
    import sys\nfrom library.two_sat import TwoSat\n\ninput = sys.stdin.readline\n\
    sys.setrecursionlimit(10 ** 6)\n\np, cnf, N, M = input().split()\nN, M = int(N),\
    \ int(M)\nsolver = TwoSat(N)\nfor _ in range(M):\n    s, t, _ = map(int, input().split())\n\
    \    if s > 0:\n        s -= 1\n    if t > 0:\n        t -= 1\n    solver.add_clause(s,\
    \ t)\n\nans = solver.solve()\nif ans is None:\n    print('s UNSATISFIABLE')\n\
    \    exit()\nA = []\nfor i in range(N):\n    if ans[i] is True:\n        A.append(i\
    \ + 1)\n    else:\n        A.append(-(i + 1))\nprint('s SATISFIABLE')\nprint(f\"\
    v {' '.join([str(a) for a in A])} 0\")\n"
  dependsOn:
  - library/two_sat.py
  isVerificationFile: true
  path: tests/yosupo/two_sat.test.py
  requiredBy: []
  timestamp: '2023-01-08 00:45:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/two_sat.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/two_sat.test.py
- /verify/tests/yosupo/two_sat.test.py.html
title: tests/yosupo/two_sat.test.py
---
