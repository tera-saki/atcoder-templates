from typing import List, Tuple
from collections import deque


class BipartiteMatching:
    # reference: https://snuke.hatenablog.com/entry/2019/05/07/013609
    def __init__(self, L: int, R: int):
        self.L = L
        self.R = R

        self.N = L + R
        self.G = [[] for _ in range(self.N)]
        self.pair_l = [None] * self.L
        self.pair_r = [None] * self.R

    def add_edge(self, a: int, b: int) -> None:
        """add edges

        Args:
            a (int): left vertex index (0 <= a < L)
            b (int): right vertex index (0 <= b < R)
        """
        assert 0 <= a < self.L
        assert 0 <= b < self.R
        self.G[a].append(b)

    def solve(self) -> int:
        ret = 0
        while True:
            pre = [None] * self.L
            root = [None] * self.L
            update = False

            dq = deque()
            for i in range(self.L):
                if self.pair_l[i] is None:
                    root[i] = i
                    dq.append(i)
            while dq:
                v = dq.popleft()
                if self.pair_l[root[v]] is not None:
                    continue
                for d in self.G[v]:
                    if self.pair_r[d] is None:
                        while d is not None:
                            self.pair_r[d] = v
                            self.pair_l[v], d = d, self.pair_l[v]
                            v = pre[v]
                        update = True
                        ret += 1
                        break
                    d = self.pair_r[d]
                    if pre[d] is not None:
                        continue
                    pre[d] = v
                    root[d] = root[v]
                    dq.append(d)
            if not update:
                break
        return ret

    def pairs(self) -> List[Tuple[int, int]]:
        p = []
        for i in range(self.L):
            pair = self.pair_l[i]
            if pair is None:
                continue
            p.append((i, pair))
        return p
