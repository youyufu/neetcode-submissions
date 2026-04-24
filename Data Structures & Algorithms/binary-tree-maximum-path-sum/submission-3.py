# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root) -> (canextend, noextend):
            #       1
            #   2       4
            # 5    4
            if not root:
                return (float('-inf'), float('-inf'))
            lsum = dfs(root.left)
            rsum = dfs(root.right)
            canextend = max(root.val, root.val+lsum[0], root.val+rsum[0])
            noextend = max(lsum[0], lsum[1], rsum[0], rsum[1], root.val+lsum[0]+rsum[0])
            return (canextend, noextend)
        
        canextend, noextend = dfs(root)
        return max(canextend, noextend)
