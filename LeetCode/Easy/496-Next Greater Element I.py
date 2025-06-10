#LINk: https://leetcode.com/problems/next-greater-element-i/

# LeetCode 496. Next Greater Element I
# Approach 1: Bit Manipulation (XOR)
# Time: O(n), Space: O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_map = {}
        stack = []

        for i in nums2[::-1]:
            while stack and stack[-1]  <= i:
                stack.pop()
            
            if stack:
                greater_map[i] = stack[-1]
            else:
                greater_map[i] = -1
            
            stack.append(i)

        result = []
