class WeightedUnionFind:
    def __init__(self, N):
        self.N = N
        self.par = [-1] * N
        self.weight = [0] * N

    def find(self, x, w=0):
        if self.par[x] < 0:
            return x, w
        else:
            return self.find(self.par[x], w + self.weight[x])

    def merge(self, x, y, z):
        "Wy = Wx + z"
        x, wx = self.find(x)
        y, wy = self.find(y)

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
        x, wx = self.find(x)
        y, wy = self.find(y)

        if x != y:
            return None
        return wy - wx

    def same(self, x, y):
        return self.find(x)[0] == self.find(y)[0]
