class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        arr = []
        n = len(costs)
        for i in range(n):
            a, b = costs[i][0], costs[i][1]
            arr.append((b-a,i))

        ans = 0
        arr.sort(reverse = True)
        mid = (n-1)//2 
        
        for i in range(mid + 1):
            index = arr[i][1]
            ans += costs[index][0]

        for i in range(mid+1,n):
            index = arr[i][1]
            ans += costs[index][1]
        return ans