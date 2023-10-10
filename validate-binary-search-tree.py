# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, lesser, greater):
            if not root:
                return True
            
            if  root.val <= lesser or root.val >= greater:
                return False
            
            else:
                return validate(root.left, lesser, root.val) and validate(root.right, root.val, greater)
            
        return validate(root, float(-inf), float(inf))