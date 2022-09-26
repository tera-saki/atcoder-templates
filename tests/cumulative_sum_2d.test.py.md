---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/cumulative_sum_2d.py
    title: library/cumulative_sum_2d.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/challenges/sources/JOI/Final/0560
    links:
    - https://onlinejudge.u-aizu.ac.jp/challenges/sources/JOI/Final/0560
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 100, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/challenges/sources/JOI/Final/0560\n\
    import sys\nfrom library.cumulative_sum_2d import CumulativeSum2D\n\ninput = sys.stdin.readline\n\
    \nH, W = map(int, input().split())\nQ = int(input())\nC = [input()[:-1] for _\
    \ in range(H)]\n\nJ = [[0 for _ in range(W)] for _ in range(H)]\nO = [[0 for _\
    \ in range(W)] for _ in range(H)]\nI = [[0 for _ in range(W)] for _ in range(H)]\n\
    for i in range(H):\n    for j in range(W):\n        if C[i][j] == 'J':\n     \
    \       J[i][j] += 1\n        elif C[i][j] == 'O':\n            O[i][j] += 1\n\
    \        else:\n            I[i][j] += 1\nSj = CumulativeSum2D(J)\nSo = CumulativeSum2D(O)\n\
    Si = CumulativeSum2D(I)\n\nfor _ in range(Q):\n    lx, ly, rx, ry = map(int, input().split())\n\
    \    lx -= 1\n    ly -= 1\n    aj = Sj.sum(lx, ly, rx, ry)\n    ao = So.sum(lx,\
    \ ly, rx, ry)\n    ai = Si.sum(lx, ly, rx, ry)\n    print(aj, ao, ai)\n"
  dependsOn:
  - library/cumulative_sum_2d.py
  isVerificationFile: true
  path: tests/cumulative_sum_2d.test.py
  requiredBy: []
  timestamp: '2022-09-26 23:57:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/cumulative_sum_2d.test.py
layout: document
redirect_from:
- /verify/tests/cumulative_sum_2d.test.py
- /verify/tests/cumulative_sum_2d.test.py.html
title: tests/cumulative_sum_2d.test.py
---