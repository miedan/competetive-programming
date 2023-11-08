# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            
            if not node:
                return 0

            left_sum = 0
            if node.left and not node.left.left and not node.left.right:
                left_sum = node.left.val

            return left_sum + recurse(node.left) + recurse(node.right)

        return recurse(root)
