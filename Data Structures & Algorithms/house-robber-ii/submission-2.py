class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robHelper(nums[:-1]), self.robHelper(nums[1:]))
    
    def robHelper(self, nums):
        rob1 = 0
        rob2 = 0
        for num in nums:
            new = max(rob2 + num, rob1)
            rob2 = rob1
            rob1 = new
        return rob1