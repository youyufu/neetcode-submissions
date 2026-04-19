class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_val = []
        for num in nums:
            if num in seen_val:
                return True
            seen_val.append(num)
        return False
         