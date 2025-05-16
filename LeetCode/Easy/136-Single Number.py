#LINk: https://leetcode.com/problems/single-number/

# LeetCode 136. Single Number
# Approach 1: Bit Manipulation (XOR)
# Time: O(n), Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

#------------------------------------------------------

# Approach 2: Hash Map (Frequency Count)
# Time: O(n), Space: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1

        for key, value in result.items():
            if value == 1:
                return key
