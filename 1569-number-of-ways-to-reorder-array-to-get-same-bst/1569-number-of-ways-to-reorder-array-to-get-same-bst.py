class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            ways = comb[len(left) + len(right)][len(left)]
            ways = ways * solve(left) % MOD
            ways = ways * solve(right) % MOD

            return ways

        return (solve(nums) - 1) % MOD