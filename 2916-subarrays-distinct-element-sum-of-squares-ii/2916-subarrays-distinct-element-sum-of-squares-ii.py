from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def apply(node, start, end, val):
            length = end - start + 1
            tree[node] += 2 * val * tree[node + 2 * 0] if False else 0

        # Each node stores (sum, sum of squares).
        sums = [0] * (4 * n)
        squares = [0] * (4 * n)

        def apply(node, start, end, val):
            length = end - start + 1
            squares[node] = (
                squares[node] + 2 * val * sums[node] + val * val * length
            ) % MOD
            sums[node] = (sums[node] + val * length) % MOD
            lazy[node] += val

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return
            mid = (start + end) // 2
            val = lazy[node]
            apply(node * 2, start, mid, val)
            apply(node * 2 + 1, mid + 1, end, val)
            lazy[node] = 0

        def update(node, start, end, left, right, val):
            if left > end or right < start:
                return
            if left <= start and end <= right:
                apply(node, start, end, val)
                return

            push(node, start, end)
            mid = (start + end) // 2
            update(node * 2, start, mid, left, right, val)
            update(node * 2 + 1, mid + 1, end, left, right, val)

            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD
            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + squares[1]) % MOD
            last[x] = i

        return ans