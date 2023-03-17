# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.cnt = defaultdict(int)
        def mode(node):
            if not node:
                return 0
            left = mode(node.left)
            right = mode(node.right)
            self.cnt[node.val] += 1
        
        mode(root)
        maxi = max(self.cnt.values())
        ans = []
        for i in self.cnt:
            if self.cnt[i] == maxi:
                ans.append(i)
        return ans
       
       
        

        
        
        
        
        
        