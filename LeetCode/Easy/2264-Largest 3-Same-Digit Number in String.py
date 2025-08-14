#LINk: https://leetcode.com/problems/largest-3-same-digit-number-in-string/

# LeetCode 2264. Largest 3-Same-Digit Number in String
# Approach 1: 
# Time: O(n), Space: O(1)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            pattern = str(digit) * 3
            if pattern in num:
                return pattern
        return ""

#------------------------------------------------------

# Approach 2:
# Time: O(n), Space: O(1)

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_triplet = ""
        for i in range(len(num) - 2):
            triplet = num[i:i+3]
            if triplet[0] == triplet[1] == triplet[2]:
                max_triplet = max(max_triplet, triplet)
        return max_triplet
