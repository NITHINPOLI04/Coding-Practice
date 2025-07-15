#LINk: https://leetcode.com/problems/longest-consecutive-sequence/

# LeetCode 128. Longest Consecutive Sequence
# Time: O(n), Space: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_sequence = 0

        for n in numbers:
            if (n - 1) not in numbers:
                length = 0
                while (n + length) in numbers:
                    length += 1
                longest_sequence = max(longest_sequence, length)
        
        return longest_sequence
