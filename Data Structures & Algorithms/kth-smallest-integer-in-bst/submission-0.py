# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def numNode(root) -> (int, int, int): # root, num_left, num_right
            if root == None:
                return (0, 0, 0)
            if root.left == None and root.right == None:
                return (1, 0, 0)
            left = numNode(root.left)
            num_left = left[0] + left[1] + left[2]
            right = numNode(root.right)
            num_right = right[0] + right[1] + right[2]
            return (1, num_left, num_right)
        
        left = numNode(root.left)
        num_left = left[0] + left[1] + left[2]
        right = numNode(root.right)
        num_right = right[0] + right[1] + right[2]

        if num_left + 1 == k:
            return root.val
        if k <= num_left:
            return self.kthSmallest(root.left, k)
        return self.kthSmallest(root.right, k - num_left - 1)