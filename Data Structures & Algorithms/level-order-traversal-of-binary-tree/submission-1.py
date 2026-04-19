# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        res.append([root.val]) # [[1]]
        # left
        # [[2], [4, 5]]
        # right
        # [[3], [6, 7]]
        left_lst = self.levelOrder(root.left)
        right_lst = self.levelOrder(root.right)
        for level in range(max(len(left_lst), len(right_lst))):
            merged = []
            if level < len(left_lst):
                merged = left_lst[level]
            if level < len(right_lst):
                merged = merged + right_lst[level]
            res.append(merged)
        return res