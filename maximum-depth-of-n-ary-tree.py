"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        
        def dfs(vertex):
            if not vertex:
                return 0
            curans = 0
            for neighbour in vertex.children:
                
                curans = max(dfs(neighbour), curans)
            return 1 + curans
        return dfs(root)