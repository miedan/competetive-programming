# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def avg(node):
            
            if not node:
                return 0,0
            left_sum, left_count = avg(node.left)
            right_sum, right_count = avg(node.right)
            
            if ((left_sum + right_sum + node.val) //(right_count + left_count + 1) == node.val):
                self.count += 1
            
            return left_sum + right_sum + node.val, right_count + left_count + 1
        
        avg(root)
        return self.count
        
       
            
            



               
            

            
    
        
        
        
        