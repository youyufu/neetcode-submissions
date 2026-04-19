class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr_lst):
            if i == len(nums):
                res.append(curr_lst.copy())
                return
            curr_lst.append(nums[i])
            dfs(i+1, curr_lst)
            curr_lst.pop()
            dfs(i+1, curr_lst)
            return
        
        dfs(0, [])
        return res