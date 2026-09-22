from typing import List


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k

        # prod[i] = product of this segment modulo k
        self.prod = [1] * (4 * self.n)

        # cnt[i][r] = number of prefixes of this segment
        # whose product % k == r
        self.cnt = [[0] * k for _ in range(4 * self.n)]

        self.nums = nums
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            value = self.nums[l] % self.k

            self.prod[node] = value
            self.cnt[node][value] = 1
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.pull(node)

    def pull(self, node):
        left = node * 2
        right = node * 2 + 1

        left_prod = self.prod[left]
        right_prod = self.prod[right]

        # Product of the whole segment
        self.prod[node] = (left_prod * right_prod) % self.k

        # First, all prefixes that end inside the left child
        for r in range(self.k):
            self.cnt[node][r] = self.cnt[left][r]

        # Then prefixes that contain all of left
        # and continue into the right child.
        #
        # If a right prefix has product r,
        # its new product is:
        #
        # left_prod * r % k
        for r in range(self.k):
            new_r = (left_prod * r) % self.k
            self.cnt[node][new_r] += self.cnt[right][r]

    def update(self, node, l, r, index, value):
        if l == r:
            value %= self.k

            self.prod[node] = value
            self.cnt[node] = [0] * self.k
            self.cnt[node][value] = 1
            return

        mid = (l + r) // 2

        if index <= mid:
            self.update(node * 2, l, mid, index, value)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, value)

        self.pull(node)

    def query(self, node, l, r, ql, qr):
        # Completely inside query range
        if ql <= l and r <= qr:
            return self.prod[node], self.cnt[node][:]

        mid = (l + r) // 2

        if qr <= mid:
            return self.query(node * 2, l, mid, ql, qr)

        if ql > mid:
            return self.query(node * 2 + 1, mid + 1, r, ql, qr)

        # Query overlaps both children
        left_prod, left_cnt = self.query(
            node * 2, l, mid, ql, qr
        )

        right_prod, right_cnt = self.query(
            node * 2 + 1, mid + 1, r, ql, qr
        )

        # Combine the two queried pieces
        result_prod = (left_prod * right_prod) % self.k

        result_cnt = left_cnt[:]

        for r in range(self.k):
            new_r = (left_prod * r) % self.k
            result_cnt[new_r] += right_cnt[r]

        return result_prod, result_cnt


class Solution:
    def resultArray(self, nums: List[int], k: int,
                    queries: List[List[int]]) -> List[int]:

        tree = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            tree.update(
                1,
                0,
                len(nums) - 1,
                index,
                value
            )

            # We need all non-empty prefixes of nums[start:]
            _, cnt = tree.query(
                1,
                0,
                len(nums) - 1,
                start,
                len(nums) - 1
            )

            ans.append(cnt[x])

        return ans