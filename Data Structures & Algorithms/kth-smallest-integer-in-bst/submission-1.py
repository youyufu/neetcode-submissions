# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_node = k
        val = root.val

        def dfs(root):
            nonlocal num_node, val
            if not root:
                return
            dfs(root.left)
            if num_node == 0:
                return
            num_node -= 1
            if num_node == 0:
                val = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return val