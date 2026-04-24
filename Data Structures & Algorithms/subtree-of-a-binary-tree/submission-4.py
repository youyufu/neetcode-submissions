# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if (root and not subRoot) or (not root and subRoot):
                return False
            if not root and not subRoot:
                return True
            return root.val == subRoot.val and isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        if not subRoot and not root:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False
        if root.val != subRoot.val and not root.left and not root.right:
            return False
        if isSameTree(root, subRoot):
            return True
        return Solution.isSubtree(self, root.left, subRoot) or Solution.isSubtree(self, root.right, subRoot)
        