#LINk: https://leetcode.com/problems/type-of-triangle/

# LeetCode 3024. Single Number
# Time: O(1), Space: O(1)

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)

        if a + b <= c:
            return 'none'

        if a == b == c:
            return 'equilateral'
        elif a == b or b == c:
            return 'isosceles'
        else:
            return 'scalene'
