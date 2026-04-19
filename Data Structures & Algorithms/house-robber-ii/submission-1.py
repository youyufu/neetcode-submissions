class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l_prev1 = 0
        l_prev2 = 0
        for i in range(len(nums)-1):
            temp = max(l_prev2+nums[i], l_prev1)
            l_prev2 = l_prev1
            l_prev1 = temp
        r_prev1 = 0
        r_prev2 = 0
        for i in range(1, len(nums)):
            temp = max(r_prev2+nums[i], r_prev1)
            r_prev2 = r_prev1
            r_prev1 = temp
        return max(l_prev1, r_prev1)