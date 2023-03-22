# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        d = defaultdict(list)
        self.traverse(root, 0, 0, d)
        for i in sorted(d.keys()):
            arr = []
            for j in sorted(d[i]):
                arr.append(j[1])
            result.append(arr)
        return result
     
    def traverse(self,root, col, row, d):
        
        if not root:
            return
       
        self.traverse(root.left, col-1, row+1, d)
        self.traverse(root.right, col+1, row+1, d)
        d[col].append((row, root.val ))
        

        
        
        
        
        
        
   