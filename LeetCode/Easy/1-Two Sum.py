#LINk: https://leetcode.com/problems/single-number/

# LeetCode 1. Two Sum
# Approach 1: Brute Force
# Time: O(n^2), Space: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#------------------------------------------------------

# Approach 2: Better Approach
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
