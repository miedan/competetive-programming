# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        que = deque([[root, 0 ]])
        maxf=-inf
        while que:
            maxf = max(maxf , (que[-1][1] - que[0][1]) + 1)
            
            allowing = len(que)
            
            while allowing > 0:
                (node , col) = que.popleft()
                 
                if node.left:
                    que.append([node.left, col*2 + 1])
                if node.right:
                    que.append([node.right, col * 2 + 2])
      
                allowing -= 1
        return maxf
        
        
        
        