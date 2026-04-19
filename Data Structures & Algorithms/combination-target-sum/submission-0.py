class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur_lst, total):
            if total == target:
                res.append(cur_lst.copy())
                return
            if total > target or i >= len(nums):
                return
            cur_lst.append(nums[i])
            dfs(i, cur_lst, total + nums[i])
            cur_lst.pop()
            dfs(i + 1, cur_lst, total)
            return
        
        dfs(0, [], 0)
        return res
