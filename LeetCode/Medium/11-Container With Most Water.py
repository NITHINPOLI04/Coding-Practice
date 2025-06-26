#LINk: https://leetcode.com/problems/container-with-most-water/

# LeetCode 11. Container With Most Water
# Approach 1: Brute Force
# Time: O(n^2), Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                wd = j - i
                ht = min(height[i], height[j])
                area = ht * wd

                max_water = max(area, max_water)

        return max_water

------------------------------------------------------

# Approach 2: Two Pointer
# Time: O(nlogn), Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        i, j = 0, len(height) - 1
            
        while i < j :    
            wd = j - i
            ht = min(height[i], height[j])
            area = ht * wd
            max_water = max(area, max_water)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_water
