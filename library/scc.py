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
        self.traverse()
        self.traverse2()

        self.C = [[] for _ in range(self.c_num)]
        for i in range(self.N):
            c = self.cid[i]
            self.C[c].append(i)

    def traverse(self):
        flag = [False] * self.N
        for i in range(self.N):
            if flag[i] is False:
                self.dfs(i, flag)
        self.V.reverse()

    def traverse2(self):
        flag = [False] * self.N
        cid = 0
        for v in self.V:
            if flag[v] is False:
                self.dfs2(v, flag)
                self.c_num += 1

    def dfs(self, v, flag):
        flag[v] = True
        for dest in self.E[v]:
            if flag[dest] is False:
                self.dfs(dest, flag)
        self.V.append(v)

    def dfs2(self, v, flag):
        flag[v] = True
        self.cid[v] = self.c_num
        for dest in self.I[v]:
            if flag[dest] is False:
                self.dfs2(dest, flag)
