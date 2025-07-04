#LINk: https://leetcode.com/problems/group-anagrams/

# LeetCode 49. Group Anagrams
# Time: O(N * K), Space: O(N * K)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default_dict = {}

        for word in strs:
            code = [0] * 26
            for char in word:
                code[ord(char) - ord('a')] += 1

            key = tuple(code)

            if key not in default_dict:
                default_dict[key] = []

            default_dict[key].append(word)

        return list(default_dict.values())
