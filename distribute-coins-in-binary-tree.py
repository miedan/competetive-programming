# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            moves = left + right + node.val - 1
            ans += abs(moves)   
            return moves

        dfs(root)
        return ans