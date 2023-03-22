# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def balance(root):
            if not root:
                return [0, True]
            left = balance(root.left)
            right = balance(root.right)
            hb = (left[1] and right[1] and abs(right[0] - left[0]) <= 1 )
            return [1 + max(right[0], left[0]), hb]
        return balance(root)[1]
        