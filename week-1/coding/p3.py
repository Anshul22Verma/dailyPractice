# problem: combination-sum
# ref: https://leetcode.com/problems/combination-sum/
from typing import List

class Solution:
    def dp(self, candidates: List[int], target: int, current: List[int]):
        if len(candidates) == 0 or target <= 0:
            return
        if sum(current) == target:
            self.result.append(current)
            return
        elif sum(current) > target:
            return
        else:
            for idx, c in enumerate(candidates):
                # if we choose to keep candidate idx in the result list
                self.dp(candidates[idx:], target, current + [c])
        return
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Dynamic Programming
        # TC: O(target * candidates)
        # SC: O(1) just saving results and scalar
        self.result = []
        self.dp(candidates, target, [])
        return self.result