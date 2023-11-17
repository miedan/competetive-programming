# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []

        def dfs(node, parent):

            if not node:
                return None

            tobe_deleted = node.val in to_delete

            if parent and not tobe_deleted:

                ans.append(node)
               

            node.left = dfs(node.left, tobe_deleted)
            node.right = dfs(node.right, tobe_deleted)

            return None if tobe_deleted else node

        dfs(root, True)
        
        return ans
