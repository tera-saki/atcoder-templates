---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/li_chao_tree.py
    title: library/li_chao_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/segment_add_get_min
    links:
    - https://judge.yosupo.jp/problem/segment_add_get_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min\n\
    import sys\nfrom library.li_chao_tree import LiChaoTree\n\ninput = sys.stdin.readline\n\
    \nN, Q = map(int, input().split())\nlines = [tuple(map(int, input().split()))\
    \ for _ in range(N)]\nquery = [tuple(map(int, input().split())) for _ in range(Q)]\n\
    X = []\nfor l, r, a, b in lines:\n    X.append(l)\n    X.append(r)\nfor t, *q\
    \ in query:\n    if t == 0:\n        l, r, a, b = q\n        X.append(l)\n   \
    \     X.append(r)\n    else:\n        p, = q\n        X.append(p)\n\nX = sorted(set(X))\n\
    solver = LiChaoTree(X)\nfor l, r, a, b in lines:\n    solver.add_line_segment((a,\
    \ b), l, r)\nfor t, *q in query:\n    if t == 0:\n        l, r, a, b = q\n   \
    \     solver.add_line_segment((a, b), l, r)\n    else:\n        p, = q\n     \
    \   v = solver.query(p)\n        print(v if v < solver.inf else 'INFINITY')\n"
  dependsOn:
  - library/li_chao_tree.py
  isVerificationFile: true
  path: tests/yosupo/segment_add_get_min.test.py
  requiredBy: []
  timestamp: '2023-01-08 11:42:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/yosupo/segment_add_get_min.test.py
layout: document
redirect_from:
- /verify/tests/yosupo/segment_add_get_min.test.py
- /verify/tests/yosupo/segment_add_get_min.test.py.html
title: tests/yosupo/segment_add_get_min.test.py
---
