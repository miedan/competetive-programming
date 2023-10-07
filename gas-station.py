class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        diff = [(gas[i] - cost[i]) for i in range(n)]

        start_index = 0
        current_gas = 0

        for i in range(n):

            current_gas += diff[i]

          
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1

        return start_index