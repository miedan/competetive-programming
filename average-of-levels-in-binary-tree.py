# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []
        
        def bfs(node):

            

            que = collections.deque()
            que.append(node)
            
            while que:
                
                summ = 0
                cur_len = len(que)

                for _ in range(cur_len):

                    node = que.popleft()
                    summ += node.val
                    

                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)

                ans.append(summ / cur_len)





        bfs(root)
        return ans