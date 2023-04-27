class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

       

        visited = set()
        visited.add(0)
        que = deque([rooms[0]])

        while que:

                rom = que.popleft()
                for i in range(len(rom)):
                    if rom[i] not in visited:
                        visited.add(rom[i])
                        que.append(rooms[rom[i]])
                        
                
           
        return len(visited) == len(rooms)