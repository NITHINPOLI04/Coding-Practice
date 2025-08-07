#LINk: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# LeetCode 3. Longest Substring Without Repeating Characters
# Time: O(n), Space: O(Min(n,m)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        max_len = 0
        start = 0

        for end in range(len(s)):
            current = s[end]

            if current in hash_map and hash_map[current] >= start:
                start = hash_map[current] + 1
            
            hash_map[current] = end
            max_len = max(max_len, end - start + 1)

        return max_len
