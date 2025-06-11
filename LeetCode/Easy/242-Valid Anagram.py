#LINk: https://leetcode.com/problems/valid-anagram/

# LeetCode 242. Valid Anagram
# Time: O(nlogn), Space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)
