class SCC:
    def __init__(self, N, E):
        self.N = N
        self.E = E
        self.I = [[] for _ in range(N)]
        for s in range(N):
            for t in E[s]:
                self.I[t].append(s)

        self.V = []
        self.cid = [None] * N
        self.c_num = 0
        self._traverse()
        self._traverse2()

        self.C = [[] for _ in range(self.c_num)]
        for i in range(self.N):
            c = self.cid[i]
            self.C[c].append(i)

    def to_dag(self):
        NE = [set() for _ in range(self.c_num)]
        for i in range(self.N):
            ci = self.cid[i]
            for j in self.E[i]:
                cj = self.cid[j]
                if ci == cj:
                    continue
                NE[ci].add(cj)
        return self.C, [list(ne) for ne in NE]

    def _traverse(self):
        flag = [False] * self.N
        for i in range(self.N):
            if not flag[i]:
                self._dfs(i, flag)
        self.V.reverse()

    def _traverse2(self):
        flag = [False] * self.N
        cid = 0
        for v in self.V:
            if not flag[v]:
                self._dfs2(v, flag)
                self.c_num += 1

    def _dfs(self, v, flag):
        stack = [~v, v]
        while stack:
            v = stack.pop()
            if v < 0:
                self.V.append(~v)
                continue

            if flag[v]:
                stack.pop()
                continue
            flag[v] = True
            for dest in self.E[v]:
                if not flag[dest]:
                    stack.append(~dest)
                    stack.append(dest)

    def _dfs2(self, v, flag):
        stack = [v]
        while stack:
            v = stack.pop()
            if flag[v]:
                continue
            flag[v] = True
            self.cid[v] = self.c_num
            for dest in self.I[v]:
                if not flag[dest]:
                    stack.append(dest)
