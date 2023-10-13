# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        prev_count = defaultdict(int)
        count = 0
        cur_sum = 0
        prev_count[0] = 1

        def dfs(node):
            nonlocal count, cur_sum



            if not node:
                return 0

            cur_sum += node.val

            if cur_sum - targetSum in prev_count:
                count += prev_count[cur_sum - targetSum]
            
            prev_count[cur_sum] += 1
            

            dfs(node.left)
            dfs(node.right)

            prev_count[cur_sum] -= 1
            cur_sum -= node.val

        dfs(root)
        return count