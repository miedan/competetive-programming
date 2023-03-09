# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or ( not q and p) or(p.val != q.val) :
            return False
        is_sameleft= self.isSameTree(p.left, q.left)
        is_sameright= self.isSameTree(p.right,q.right)

        return is_sameleft and is_sameright
       