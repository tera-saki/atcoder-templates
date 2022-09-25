from typing import List

from library.scc import SCC


class TwoSat:
    def __init__(self, N: int):
        self.N = N
        self.E = [[] for _ in range(2 * N)]

    def add_clause(self, s: int, t: int) -> None:
        def vid(n):
            return 2 * (~n) + 1 if n < 0 else 2 * n

        def oppose(id):
            return id ^ 1

        sid, tid = vid(s), vid(t)
        # ~s -> t
        self.E[oppose(sid)].append(tid)
        # ~t -> s
        self.E[oppose(tid)].append(sid)

    def solve(self) -> List[bool]:
        cid = SCC(2 * self.N, self.E).cid
        for i in range(self.N):
            if cid[2 * i] == cid[2 * i + 1]:
                return None
        # if cid[2 * a] > cid[2 * a + 1], possibly ~a -> a
        ans = [cid[2 * i] > cid[2 * i + 1] for i in range(self.N)]
        return ans
