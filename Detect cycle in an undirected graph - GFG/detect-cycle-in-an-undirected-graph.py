from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		n = len(adj)
		visited = set()
		
		def cycle(node, parent):
		    
		    if node in visited:
		        return True
		    
		    visited.add(node)
		    
            for neigh in adj[node]:
                if neigh != parent:
                    if cycle(neigh, node):
                        return True
                    
            return False
	  
		    
		for i in range(n):
		    
		    if i not in visited:
		        if cycle(i,None):
		            return 1
			    
		   
		return 0
		
		

		    
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends