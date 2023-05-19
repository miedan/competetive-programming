class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
    
        parent = [i for i in range(26)]
        
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(v1, v2):

            parentv1 =  find(v1)
            parentv2 = find(v2)

            parent[parentv1] = parentv2

        for s in equations:

            if s[1] == "=":
                union(ord(s[0])- ord('a'), ord(s[3]) - ord('a'))

        for s in equations:
            if s[1] == "!":
                if find(ord(s[0])- ord('a')) == find(ord(s[3]) - ord('a')):
                    return False
         
            
                
        return True