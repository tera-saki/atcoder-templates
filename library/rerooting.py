import sys
from typing import List, Callable, TypeVar

T = TypeVar('T')

input = sys.stdin.readline


class Rerooting:
    # reference: https://null-mn.hatenablog.com/entry/2020/04/14/124151
    # 適当な頂点vを根とする部分木に対して計算される値dp_vが、vの子c1, c2, ... ckを用いて
    # 下記のように表すことができる
    # dp_v = g(merge(f(dp_c1,c1), f(dp_c2,c2), ..., f(dp_ck,ck)), v)
    def __init__(self, N: int, E: List[List[int]],
                 f: Callable[[T, int], T],
                 g: Callable[[T, int], T],
                 merge: Callable[[T, T], T], e: T):
        self.N = N
        self.E = E
        self.f = f
        self.g = g
        self.merge = merge
        self.e = e

        self.dp = [[self.e for _ in range(len(self.E[v]))] for v in range(self.N)]
        self._calculate()

    # def _dfs1(self, v, p):
    #     # ある頂点の根付き木として、ぞれぞの頂点の値を求める
    #     acc = self.e
    #     for i, d in enumerate(self.E[v]):
    #         if d == p:
    #             continue
    #         self.dp[v][i] = self._dfs1(d, v)
    #         acc = self.merge(acc, self.f(self.dp[v][i], d))
    #     return self.g(acc, v)

    def _dfs1(self, root):
        stack = [(root, -1)]
        ret = [self.e] * self.N
        while stack:
            v, p = stack.pop()
            if v < 0:
                v = ~v
                acc = self.e
                for i, d in enumerate(self.E[v]):
                    if d == p:
                        continue
                    self.dp[v][i] = ret[d]
                    acc = self.merge(acc, self.f(ret[d], d))
                ret[v] = self.g(acc, v)
                continue

            stack.append((~v, p))
            for i, d in enumerate(self.E[v]):
                if d == p:
                    continue
                stack.append((d, v))

    # def _dfs2(self, v, p, from_par):
    #     # それぞれの頂点を根としてみた時の値を求める
    #     for i, d in enumerate(self.E[v]):
    #         if d == p:
    #             self.dp[v][i] = from_par
    #             break
    #     c = len(self.E[v])
    #     # 子を右からなめた場合の累積値
    #     Sr = [self.e] * (c + 1)
    #     for i in range(c, 0, -1):
    #         Sr[i - 1] = self.merge(Sr[i], self.f(self.dp[v][i - 1], self.E[v][i - 1]))
    #     Sl = self.e
    #     for i, d in enumerate(self.E[v]):
    #         if d != p:
    #             val = self.merge(Sl, Sr[i + 1])
    #             self._dfs2(d, v, self.g(val, v))
    #         Sl = self.merge(Sl, self.f(self.dp[v][i], d))

    def _dfs2(self, root):
        stack = [(root, -1, self.e)]
        while stack:
            v, p, from_par = stack.pop()
            for i, d in enumerate(self.E[v]):
                if d == p:
                    self.dp[v][i] = from_par
                    break
            c = len(self.E[v])
            Sr = [self.e] * (c + 1)
            for i in range(c, 0, -1):
                Sr[i - 1] = self.merge(Sr[i], self.f(self.dp[v][i - 1], self.E[v][i - 1]))
            Sl = self.e
            for i, d in enumerate(self.E[v]):
                if d != p:
                    val = self.merge(Sl, Sr[i + 1])
                    stack.append((d, v, self.g(val, v)))
                Sl = self.merge(Sl, self.f(self.dp[v][i], d))

    def _calculate(self, root=0):
        self._dfs1(root)
        self._dfs2(root)

    def solve(self, v):
        ans = self.e
        for i, d in enumerate(self.E[v]):
            ans = self.merge(ans, self.f(self.dp[v][i], d))
        return self.g(ans, v)
