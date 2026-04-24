class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        realt = 0
        for i in range(len(nums)+1):
            if i < len(nums):
                total += nums[i]
            realt += i
        return realt - total
