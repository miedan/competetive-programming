"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        adjlist = defaultdict(list)
        imp = defaultdict(int)
        
        for i in employees:
            imp[i.id] = i.importance
            adjlist[i.id] = i.subordinates
            
        self.summ = 0
        def dfs(vertex):

            if not adjlist[vertex]:
                self.summ += imp[vertex]
                return self.summ
            self.summ += imp[vertex]
            for neighbour in adjlist[vertex]:
                dfs(neighbour)
            return self.summ

        return dfs(id)