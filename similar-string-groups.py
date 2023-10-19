class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        parent = [i for i in range(len(strs))]

        group = len(strs)

        def find(x):
            
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            nonlocal group
            parent_x = find(x)
            parent_y = find(y)
        
            group -= parent_x != parent_y   

            parent[parent_x] = parent[parent_y]


        for i in range(len(strs)):

            for j in range(i + 1, len(strs)):
                
                swap_count = 0

                tobe_swapped = strs[i]
                tobe_checked = strs[j]

                for k in range(len(tobe_swapped)):

                    if tobe_swapped[k] != tobe_checked[k]:
                        swap_count += 1

                    if swap_count > 2:
                        break
                # print(swap_count)
                if swap_count <= 2:
                    union(i,j)

        

        return group