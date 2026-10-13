class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        total=0
        nums.sort(key=lambda x:x*x,reverse=True)
        for i in range(len(nums)):
            if i<(len(nums)+1)//2:
                total+=nums[i]**2
            else:
                total-=nums[i]**2
        return total        