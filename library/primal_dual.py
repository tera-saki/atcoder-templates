import heapq


class PrimalDual:
    def __init__(self, N, inf=1 << 50):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.inf = inf

    def add_edge(self, u, v, cap, cost):
        assert cap >= 0 and cost >= 0
        forward = [cap, v, cost, None]
        backward = [0, u, -cost, None]
        forward[3] = backward
        backward[3] = forward
        self.G[u].append(forward)
        self.G[v].append(backward)

    def flow(self, s, t, f):
        ret = 0
        H = [0] * self.N
        prev = [None] * self.N

        while f:
            C = [self.inf] * self.N
            visited = [False] * self.N
            C[s] = 0
            h = [(0, s)]

            while h:
                _, v = heapq.heappop(h)
                if visited[v]:
                    continue
                visited[v] = True

                for e in self.G[v]:
                    cap, d, cost, _ = e
                    if cap <= 0:
                        continue
                    nc = C[v] + cost + H[v] - H[d]
                    if C[d] > nc:
                        C[d] = nc
                        prev[d] = (v, e)
                        heapq.heappush(h, (C[d], d))

            if not visited[t]:
                return None

            for i in range(self.N):
                H[i] += C[i]

            min_cap = f
            cur = t
            while cur != s:
                pv, pe = prev[cur]
                min_cap = min(min_cap, pe[0])
                cur = pv
            f -= min_cap
            ret += min_cap * H[t]

            cur = t
            while cur != s:
                pv, pe = prev[cur]
                pe[0] -= min_cap
                pe[3][0] += min_cap
                cur = pv
        return ret
