class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[pos, spd] for pos, spd in zip(position, speed)]
        
        stack = []
        for pos, spd in sorted(pair) [:: -1]:
            stack.append((target - pos) / spd)
            if len(stack) >1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        