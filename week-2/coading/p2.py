# problem: Next Permutation
# ref: https://leetcode.com/problems/next-permutation/
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        TC: O(N)
        SC: O(1)
        """
        # [1, 2, 3, 4, 5] -> [1, 2, 3, 5, 4]
        # [7, 6, 4, 5, 8, 1, 0] -> [7, 6, 4, 8, 5, 0, 1]
        # if the entire list is in deacreasing order then reverse the list
        # if not go from the right find the first non-increasing pair and flip them
        # flip the remaining part of the array

        # Step 1: Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # There is a valid pivot
            # Step 2: Find the element to swap with
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap the pivot and the larger element
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the portion after index i
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums