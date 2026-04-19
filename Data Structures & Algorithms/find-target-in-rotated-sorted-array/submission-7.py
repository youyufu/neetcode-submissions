class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1, 2, 3, 4], target = 3
        # [1, 2, 3, 4], target = 1
        # [5, 6, 1, 2, 3, 4], target = 6
        # [3, 4, 5, 6, 1, 2], target = 1
        i = 0
        j = len(nums) - 1
        ind = -1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                ind = mid
                break
            if nums[mid] >= nums[i]:
                if target < nums[mid] and target >= nums[i]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return ind