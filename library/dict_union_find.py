from collections import defaultdict


class UnionFindDict:
    def __init__(self):
        self.par = defaultdict(lambda: -1)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def roots(self):
        return [k for k, v in self.par.items() if v < 0]

    def members(self, x):
        p = self.find(x)
        return [k for k in self.par if self.find(k) == p]
