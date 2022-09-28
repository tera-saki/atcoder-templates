from typing import List

from library.scc import SCC


class TwoSat:
    def __init__(self, N: int):
        self.N = N
        self.E = [[] for _ in range(2 * N)]

    def vid(self, n):
        return 2 * (~n) + 1 if n < 0 else 2 * n

    def add_clause(self, s: int, t: int) -> None:
        sid, tid = self.vid(s), self.vid(t)
        # ~s -> t
        self.E[sid ^ 1].append(tid)
        # ~t -> s
        self.E[tid ^ 1].append(sid)

    def if_then(self, s: int, t: int) -> None:
        sid, tid = self.vid(s), self.vid(t)
        self.add_clause(~s, t)

    def solve(self) -> List[bool]:
        cid = SCC(2 * self.N, self.E).cid
        for i in range(self.N):
            if cid[2 * i] == cid[2 * i + 1]:
                return None
        # if cid[2 * a] > cid[2 * a + 1], possibly ~a -> a
        ans = [cid[2 * i] > cid[2 * i + 1] for i in range(self.N)]
        return ans
