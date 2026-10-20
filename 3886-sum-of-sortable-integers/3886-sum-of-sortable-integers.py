
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        divisors = []
        for k in range(1, int(n ** 0.5) + 1):
            if n % k == 0:
                divisors.append(k)
                if k != n // k:
                    divisors.append(n // k)

        for k in divisors:
            valid = True
            prev_max = None

            for start in range(0, n, k):
                block = nums[start:start + k]
                m = len(block)

                # A block must have at most one circular descent.
                descents = 0
                for i in range(m):
                    if block[i] > block[(i + 1) % m]:
                        descents += 1
                        if descents > 1:
                            valid = False
                            break

                if not valid:
                    break

                # Blocks must also be in the correct global order.
                block_min = min(block)
                block_max = max(block)

                if prev_max is not None and prev_max > block_min:
                    valid = False
                    break

                prev_max = block_max

            if valid:
                ans += k

        return ans
