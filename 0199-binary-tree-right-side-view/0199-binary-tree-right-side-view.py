# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = collections.deque()
        que.append(root)
        
        while que:
            temp = []
            curr_len = len(que)
            for i in range(curr_len) :
                
                node = que.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:    
                        que.append(node.right)
            if temp:
                res.append(temp[-1])
        return res
                