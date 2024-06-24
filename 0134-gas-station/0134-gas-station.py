class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_tank, current_tank = 0, 0
        starting_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # If one couldn't get here
            if current_tank < 0:
                # Pick up the next station as the starting one
                starting_station = i + 1
                # Reset current tank
                current_tank = 0

        return starting_station if total_tank >= 0 else -1