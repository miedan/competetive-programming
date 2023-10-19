class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        parent = [i for i in range(len(strs))]

        def find(x):
            
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):

            parnet_x = find(x)
            parent_y = find(y)
        

            parent[parnet_x] = parent[parent_y]


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

        for i in range(len(parent)):
            find(i)

        group = set()

        for p in parent:
            group.add(p)

        return len(group)