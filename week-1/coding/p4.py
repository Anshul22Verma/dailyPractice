# ref: https://leetcode.com/problems/gas-station
# ref: https://www.youtube.com/watch?v=lJwbPZGo05A
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:   
        """
        TC: O(N) -> Tricky problem "Greedy"
        SC: O(1)
        """     
        if sum(gas) < sum(cost):
            return -1
        
        current_gas = 0
        start_idx = 0
        for idx in range(len(gas)):
            current_gas += gas[idx] - cost[idx]
            
            if current_gas < 0:
                current_gas = 0
                start_idx = idx + 1
        return start_idx
        