class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_len = [1] * len(nums)
        for i in range(1, len(nums)):
            curr_max = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    curr_max = max(curr_max, max_len[j] + 1)
            max_len[i] = curr_max
        return max(max_len)
            