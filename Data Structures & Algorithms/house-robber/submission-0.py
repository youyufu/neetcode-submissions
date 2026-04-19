class Solution:
    def rob(self, nums: List[int]) -> int:
        max_prev2 = 0
        max_prev1 = 0
        for i in range(0, len(nums)):
            curr_max = max(max_prev2 + nums[i], max_prev1)
            max_prev2 = max_prev1
            max_prev1 = curr_max
        return max_prev1