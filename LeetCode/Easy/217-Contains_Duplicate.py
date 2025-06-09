#LINk: https://leetcode.com/problems/contains-duplicate/

# LeetCode 217. Contains Duplicate
# Approach 1: 
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}

        for i in nums:
            if i in result:
                return True
            else:
                result[i] = 1
        
        return False

#------------------------------------------------------

# Approach 2:
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
