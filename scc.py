class SCC:
    def __init__(self, N, E):
        self.N = N
        self.E = E
        self.I = [[] for _ in range(N)]
        for s in range(N):
            for t in E[s]:
                self.I[t].append(s)
        
        self.V = []
        self.C = []
        self.traverse()
        self.traverse2()

    def toDAG(self):
        cidx = [None] * self.N
        for i in range(len(self.C)):
            for v in self.C[i]:
                cidx[v] = i
        edge = [set() for _ in range(len(self.C))]
        for v in range(self.N):
            cv = cidx[v]
            for dest in self.E[v]:
                cdest = cidx[dest]
                if cv == cdest:
                    continue
                edge[cv].add(cdest)
        edge = [list(s) for s in edge]
        return self.C, edge

    def traverse(self):
        flag = [False] * self.N
        for i in range(self.N):
            if flag[i] is False:
                self.dfs(i, flag)
        self.V.reverse()

    def traverse2(self):
        flag = [False] * self.N
        for v in self.V:
            if flag[v] is False:
                idx = len(self.C)
                self.C.append([])
                self.dfs2(idx, v, flag)

    def dfs(self, v, flag):
        flag[v] = True
        for dest in self.E[v]:
            if flag[dest] is False:
                self.dfs(dest, flag)
        self.V.append(v)

    def dfs2(self, idx, v, flag):
        flag[v] = True
        self.C[idx].append(v)
        for dest in self.I[v]:
            if flag[dest] is False:
                self.dfs2(idx, dest, flag)
