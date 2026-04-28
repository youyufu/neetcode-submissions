class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        res = nums[0]
        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum += num
            res = max(res, currsum)
        return res