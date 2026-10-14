
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        ans = ""

        while num > 0:
            digit = min(9, sum)
            ans += str(digit)
            sum -= digit
            num -= 1

        return ans
