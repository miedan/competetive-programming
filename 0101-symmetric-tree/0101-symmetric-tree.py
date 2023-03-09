# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        check = self.issym(root.left, root.right)
        return check
        
    def issym(self,r1, r2):
        if not r1 and not r2:
            return True
        if (not r1 and r2) or ( not r2 and r1) or (r1.val != r2.val):
            return False        

        is_sameright = self.issym(r1.left, r2.right)
        is_sameleft = self.issym(r1.right, r2.left)
        return is_sameright and is_sameleft
    
           
            

        
        
       
        
      