#LINk: https://leetcode.com/problems/max-consecutive-ones/

# LeetCode 485. Max Consecutive Ones
# Approach 1: 
# Time: O(n), Space: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        
        return max_count

#------------------------------------------------------

# Approach 2: Using 2-pointer approach
# Time: O(n), Space: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
            max_len = max(max_len, right - left + 1)

        return max_len
