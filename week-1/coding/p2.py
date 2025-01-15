# problem: Container With Most Water
# ref: https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer problem
        # SC: O(1), constant space as we are not saving anything
        # TC: O(N), where N is numbrt of vertical lines
        i, j = 0, len(height) - 1
        max_water = 0
        while i < j:
            water = (j-i) * min(height[i], height[j])
            if water > max_water:
                max_water = water
            
            if height[i] <= height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
        return max_water
