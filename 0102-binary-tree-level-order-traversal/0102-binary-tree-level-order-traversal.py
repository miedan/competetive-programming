# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def trversal(node, level):
            if not node:
                return
            
            if level >= len(result):
                result.append([])
            
            result[level].append(node.val)
            trversal(node.left, level+1)
            trversal(node.right, level+1)
            
        trversal(root, 0)
        return result