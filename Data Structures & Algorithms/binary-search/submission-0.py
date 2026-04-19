class Solution:
    def binary_search(nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        else:
            half = len(nums) // 2
            l_idx = Solution.binary_search(nums[:half], target)
            r_idx = Solution.binary_search(nums[half:], target)
            if l_idx != -1:
                return l_idx
            if r_idx != -1:
                return half + r_idx
            else:
                return -1

    def search(self, nums: List[int], target: int) -> int:
        return Solution.binary_search(nums, target)