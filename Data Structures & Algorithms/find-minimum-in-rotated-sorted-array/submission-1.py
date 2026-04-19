class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        curr_min = nums[l]
        if l == r:
            return curr_min
        while l <= r:
            mid = (l + r) // 2
            if mid + 1 == len(nums):
                break
            if nums[mid] > nums[mid+1]:
                curr_min = nums[mid+1]
                break
            elif nums[mid] < nums[0]:
                r = mid - 1
            else:
                l = mid + 1
        return curr_min
# [6, 1, 2, 3, 4, 5]