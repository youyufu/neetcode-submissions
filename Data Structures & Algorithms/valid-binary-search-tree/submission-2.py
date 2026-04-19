# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        check = self.valid_minmax(root)
        return check[0]
    
    def valid_minmax(self, root) -> (bool, Optional[int], Optional[int]):
        if root == None:
            return (True, None, None)
        if root.left == None and root.right == None:
            return (True, root.val, root.val)
        l_check = self.valid_minmax(root.left)
        r_check = self.valid_minmax(root.right)
        if not (l_check[0] and r_check[0]):
            return (False, root.val, root.val)
        if (l_check[2] != None and l_check[2] >= root.val) or (r_check[1] != None and r_check[1] <= root.val):
            return (False, root.val, root.val)
        min_val = root.val
        if l_check[1] != None:
            min_val = l_check[1]
        max_val = root.val
        if r_check[2] != None:
            max_val = r_check[2]
        return (True, min_val, max_val)