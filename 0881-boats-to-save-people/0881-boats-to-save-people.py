class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        left, right = 0, len(people)-1
        
        while left <= right:
            weight = limit - people[right]
            right -=1
            boat +=1
            if  weight >= people[left]:
                left+=1
        return boat
            
        
        