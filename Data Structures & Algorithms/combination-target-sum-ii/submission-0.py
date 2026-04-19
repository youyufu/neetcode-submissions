class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr_lst, curr_sum): # [1, 1, 2, 1, 3] -> [1, 1, 1, 2, 3]
            if curr_sum == target:
                res.append(curr_lst.copy())
                return
            if i == len(candidates) or curr_sum > target:
                return
            curr_lst.append(candidates[i])
            dfs(i+1, curr_lst, curr_sum + candidates[i])
            curr_lst.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, curr_lst, curr_sum)
            return
        
        dfs(0, [], 0)
        return res