class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent = [i for i in range(26)]

       
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
                

        def union(v1, v2):

            parentv1 = find(v1)
            parentv2 = find(v2)

            if parentv1 > parentv2:
                parent[parentv1] = parentv2 
            else:
                parent[parentv2] = parentv1

        for i in range(len(s1)):
            union(ord(s1[i]) - ord('a'), ord( s2[i]) - ord('a'))
       

        str_ = ""
        for s in baseStr:
            str_ += chr(find(ord(s) - ord('a')) + ord('a'))
        return str_