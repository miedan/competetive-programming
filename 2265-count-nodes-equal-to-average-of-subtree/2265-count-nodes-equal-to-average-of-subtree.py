# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        # self.count = 0
        
        def avg(node): 
            if not node:
                return [0,0,0]
            
            total_left = avg(node.left)
            
            total_right = avg(node.right)
            arr = [0]*3
            no_node = total_left[1]+total_right[1]+1
            total_sum = total_left[0] + total_right[0] + node.val
            average = ( total_sum)//(no_node)
            arr[0] = total_sum
            arr[1] = no_node
            arr[2] = total_left[2] + total_right[2]
        
            if average == node.val:
                arr[2] += 1
                
            return arr 
            
        res=avg(root)  
        
        return res[2]
            
            
            
            
            
            
        
            
            



               
            

            
    
        
        
        
        