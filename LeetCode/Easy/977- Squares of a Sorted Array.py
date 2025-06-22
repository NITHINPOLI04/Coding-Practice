#LINk: https://leetcode.com/problems/squares-of-a-sorted-array/

# LeetCode 977. Squares of a Sorted Array
# Approach 1: Brute Force
# Time: O(nlogn), Space: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        return sorted(nums)

#------------------------------------------------------

# Approach 2: Better Approach
# Time: O(n), Space: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            
            pos -= 1

        return result
