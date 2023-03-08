# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower = -inf, upper = inf) -> bool:
        stack = [[root,lower, upper]]
        flag = True
        
        while stack:
            [r,low ,upp ] = stack.pop()
            if not r:
                continue
            if (r.val <= low) or (r.val >= upp):
                 return  False
            stack.append([r.left, low, r.val])
            stack.append([r.right, r.val, upp])
        return flag

            



            
    




        
    
        




