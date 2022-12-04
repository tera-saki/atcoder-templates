class WeightedUnionFind:
    def __init__(self, N):
        self.N = N
        self.par = [-1] * N
        self.weight = [0] * N

    def find(self, x):
        if self.par[x] < 0:
            return x
        p = self.find(self.par[x])
        self.weight[x] += self.weight[self.par[x]]
        self.par[x] = p
        return self.par[x]

    def merge(self, x, y, z):
        "Wy = Wx + z"
        x_, y_ = x, y
        x = self.find(x)
        y = self.find(y)
        wx = self.weight[x_]
        wy = self.weight[y_]

        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
            wx, wy = wy, wx
            z = -z

        self.par[x] += self.par[y]
        self.par[y] = x
        self.weight[y] = z + wx - wy
        return True

    def diff(self, x, y):
        "return Wy - Wx if calculable otherwise None"
        if self.find(x) != self.find(y):
            return None
        return self.weight[y] - self.weight[x]
