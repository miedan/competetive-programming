# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []

        def dfs(node, target, path):

            nonlocal targetSum
            
            if not node:
                return []

            target += node.val
            path.append(node.val)

           
                         
            if target == targetSum and (not node.left and not node.right):

                # print(target, path)
                ans.append(path.copy())
                return path
     
            if node.left:
                # print(path)         
                dfs(node.left, target , path)
                path.pop()
                
               
            if node.right:
                # print(path)         
                dfs(node.right, target, path)
                path.pop()
               
          
        dfs(root, 0, [])
        return ans