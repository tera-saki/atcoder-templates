---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_3_a.test.py
    title: tests/aoj/grl_3_a.test.py
  - icon: ':heavy_check_mark:'
    path: tests/aoj/grl_3_b.test.py
    title: tests/aoj/grl_3_b.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/biconnected_components.test.py
    title: tests/yosupo/biconnected_components.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/cycle_detection_undirected.test.py
    title: tests/yosupo/cycle_detection_undirected.test.py
  - icon: ':heavy_check_mark:'
    path: tests/yosupo/two_edge_connected_components.test.py
    title: tests/yosupo/two_edge_connected_components.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://codeforces.com/blog/entry/68138
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple, Optional\n\n\nclass DFSTree:\n    # cf: https://codeforces.com/blog/entry/68138\n\
    \    def __init__(self, N: int):\n        self.N = N\n        self.edges = []\n\
    \n        self.E = [[] for _ in range(self.N)]\n        # span-edge and back-edge\
    \ (directed)\n        self.span_edge = [[] for _ in range(self.N)]\n        self.back_edge\
    \ = [[] for _ in range(self.N)]\n\n        self.ord = [-1] * self.N\n        self.low\
    \ = [-1] * self.N\n        self.par = [None] * self.N\n\n        self.is_art =\
    \ [False] * self.N\n        self.is_bridge = []\n\n        self.built = False\n\
    \n    def add_edge(self, u: int, v: int) -> None:\n        \"\"\"add edge\"\"\"\
    \n        eid = len(self.edges)\n        self.edges.append((u, v))\n        self.E[u].append((v,\
    \ eid))\n        self.E[v].append((u, eid))\n        self.is_bridge.append(False)\n\
    \n    def build(self) -> None:\n        \"\"\"build dfs tree\"\"\"\n        cnt\
    \ = 0\n        self.tvcc_id = [-1] * len(self.edges)\n        self.bcc_num = 0\n\
    \        for i in range(self.N):\n            if ~self.ord[i]:\n             \
    \   continue\n            stack = [(i, -1, -1)]\n            estack = []\n   \
    \         while stack:\n                v, p, p_eid = stack.pop()\n          \
    \      if v < 0:\n                    v = ~v\n                    for d, i in\
    \ self.span_edge[v]:\n                        if d == p:\n                   \
    \         continue\n                        self.low[v] = min(self.low[v], self.low[d])\n\
    \                    if ~p and self.ord[p] <= self.low[v]:\n                 \
    \       while True:\n                            eid = estack.pop()\n        \
    \                    self.tvcc_id[eid] = self.bcc_num\n                      \
    \      if eid == p_eid:\n                                break\n             \
    \           self.bcc_num += 1\n                else:\n                    if ~self.ord[v]:\n\
    \                        continue\n                    self.ord[v] = cnt\n   \
    \                 self.low[v] = cnt\n                    cnt += 1\n          \
    \          # p -> v is span-edge.\n                    if ~p:\n              \
    \          self.par[v] = (p, p_eid)\n                        self.span_edge[p].append((v,\
    \ p_eid))\n                        estack.append(p_eid)\n                    stack.append((~v,\
    \ p, p_eid))\n\n                    for d, eid in self.E[v][::-1]:\n         \
    \               if eid == p_eid:\n                            continue\n     \
    \                   if ~self.ord[d]:\n                            # v -> d is\
    \ back-edge since v is already visited.\n                            self.back_edge[v].append((d,\
    \ eid))\n                            self.low[v] = min(self.low[v], self.ord[d])\n\
    \                            estack.append(eid)\n                            continue\n\
    \                        stack.append((d, v, eid))\n\n        self._search_bridge()\n\
    \        self._search_articulation_points()\n        self.built = True\n\n   \
    \ def bridges(self) -> List[Tuple[int, int]]:\n        \"\"\"return list of edges\
    \ that are bridges\"\"\"\n        assert self.built\n        return [e for i,\
    \ e in enumerate(self.edges) if self.is_bridge[i]]\n\n    def articulation_points(self)\
    \ -> List[int]:\n        \"\"\"return list of vertices that are articulation points\"\
    \"\"\n        assert self.built\n        return [i for i in range(self.N) if self.is_art[i]]\n\
    \n    def two_edge_connected_components(self) -> List[List[int]]:\n        assert\
    \ self.built\n        tecc_id = [-1] * self.N\n        cnt = 0\n        for i\
    \ in range(self.N):\n            if ~tecc_id[i]:\n                continue\n \
    \           stack = [i]\n            while stack:\n                v = stack.pop()\n\
    \                if ~tecc_id[v]:\n                    continue\n             \
    \   tecc_id[v] = cnt\n                for d, eid in self.E[v]:\n             \
    \       if ~tecc_id[d] or self.is_bridge[eid]:\n                        continue\n\
    \                    stack.append(d)\n            cnt += 1\n        ret = [[]\
    \ for _ in range(cnt)]\n        for i, tid in enumerate(tecc_id):\n          \
    \  assert ~tid\n            ret[tid].append(i)\n        return ret\n\n    def\
    \ biconnected_components(self) -> List[List[int]]:\n        assert self.built\n\
    \        ret = [set() for _ in range(self.bcc_num)]\n        for eid, tid in enumerate(self.tvcc_id):\n\
    \            assert ~tid\n            u, v = self.edges[eid]\n            ret[tid].add(u)\n\
    \            ret[tid].add(v)\n        ret = [list(s) for s in ret]\n        for\
    \ i in range(self.N):\n            if not self.E[i]:\n                ret.append([i])\n\
    \        return ret\n\n    def _search_bridge(self) -> None:\n        for u in\
    \ range(self.N):\n            for v, i in self.span_edge[u]:\n               \
    \ # (u, v) is bridge if vertex u has child v\n                # that does not\
    \ have lowlink to pass over its parent\n                self.is_bridge[i] = self.ord[u]\
    \ < self.low[v]\n\n    def _search_articulation_points(self) -> None:\n      \
    \  for u in range(self.N):\n            if self.par[u] is None:\n            \
    \    self.is_art[u] = len(self.span_edge[u]) >= 2\n            else:\n       \
    \         for v, _ in self.span_edge[u]:\n                    if self.ord[u] <=\
    \ self.low[v]:\n                        self.is_art[u] = True\n              \
    \          break\n"
  dependsOn: []
  isVerificationFile: false
  path: library/dfs_tree.py
  requiredBy: []
  timestamp: '2023-01-05 18:27:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - tests/aoj/grl_3_b.test.py
  - tests/aoj/grl_3_a.test.py
  - tests/yosupo/two_edge_connected_components.test.py
  - tests/yosupo/cycle_detection_undirected.test.py
  - tests/yosupo/biconnected_components.test.py
documentation_of: library/dfs_tree.py
layout: document
redirect_from:
- /library/library/dfs_tree.py
- /library/library/dfs_tree.py.html
title: library/dfs_tree.py
---
