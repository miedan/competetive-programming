# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = self.traversal(root)
        # print(result)
        return result[k - 1]
    
    def traversal(self, root):
        if not root:
            return []
        curr = [root.val]
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        return left + curr + right