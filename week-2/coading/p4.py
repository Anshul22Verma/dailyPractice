# problem: 3sum
# ref: https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            TC: O(N^2)
            SC: O(1)
        """
        nums.sort()  # O(nlogn)
        res = set()

        # O(N**2)
        for i in range(len(nums)-2):
            sum_ = -nums[i] # need to get -nums by the other two numbers
            j, k = i+1, len(nums)-1
            while j < k:
                if sum_ == nums[j] + nums[k]:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[j] + nums[k] > sum_:
                    k -= 1
                elif nums[j] + nums[k] < sum_:
                    j += 1
        return [list(r) for r in res]