
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            best_size = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > best_size:
                        best_size = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = cur
                cur += 1
                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))
                u = heavy[u]

        seg = [0] * (2 * n)
        for u in range(n):
            seg[n + pos[u]] = 1 << (ord(s[u]) - ord('a'))

        for i in range(n - 1, 0, -1):
            seg[i] = seg[i * 2] ^ seg[i * 2 + 1]

        def update(p, value):
            p += n
            seg[p] = value
            p //= 2
            while p:
                seg[p] = seg[p * 2] ^ seg[p * 2 + 1]
                p //= 2

        def range_xor(l, r):
            result = 0
            l += n
            r += n
            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= seg[r]
                l //= 2
                r //= 2
            return result

        def path_xor(u, v):
            result = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                result ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u
            result ^= range_xor(pos[u], pos[v] + 1)
            return result

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(pos[u], 1 << (ord(c) - ord('a')))
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_xor(u, v)
                ans.append((mask & (mask - 1)) == 0)

        return ans
