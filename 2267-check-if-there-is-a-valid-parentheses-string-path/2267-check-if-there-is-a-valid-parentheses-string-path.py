class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # A valid parentheses string must have even length.
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] = set of possible open-parenthesis balances
        # when reaching cell (i, j).
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if grid[i][j] == ')':
                        continue
                    dp[j].add(1)
                    continue

                current = set()

                # From above
                if i > 0:
                    current.update(dp[j])

                # From left
                if j > 0:
                    current.update(dp[j - 1])

                if not current:
                    continue

                if grid[i][j] == '(':
                    new_balances = {b + 1 for b in current}
                else:
                    new_balances = {b - 1 for b in current if b > 0}

                # A balance can never exceed the number of cells
                # remaining, otherwise it cannot return to zero.
                remaining = (m - 1 - i) + (n - 1 - j)
                dp[j] = {b for b in new_balances if b <= remaining}

        return 0 in dp[n - 1]
