class EulerTour:
    def __init__(self, N, E, root=0):
        self.N = N
        self.E = E
        self.root = root
        self.D = [0] * N
        self.IN = [None] * N
        self.OUT = [None] * N

        self._traverse()

    def get_range(self, v):
        return (self.IN[v], self.OUT[v])

    def _traverse(self):
        stack = [(self.root, -1)]
        cnt = 0
        while stack:
            v, p = stack.pop()
            if v < 0:
                self.OUT[~v] = cnt
                cnt += 1
                continue

            self.IN[v] = cnt
            cnt += 1
            stack.append((~v, p))

            if p >= 0:
                self.D[v] = self.D[p] + 1
            for d in self.E[v][::-1]:
                if d == p:
                    continue
                stack.append((d, v))
