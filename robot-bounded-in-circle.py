class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

     
        direction = (0,1)
        
        position = [0,0]
        
        for ch in instructions:

            if ch == 'G':

                position[0] += direction[0]
                position[1] += direction[1]

            elif ch == 'L':

                direction = (-direction[1], direction[0])
                
            elif ch == 'R':
                direction = (direction[1], -direction[0])
        
        return position == [0,0] or direction != (0,1)