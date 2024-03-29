class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
    
        start, total_gas, tank = 0, 0, 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start if total_gas >= 0 else -1