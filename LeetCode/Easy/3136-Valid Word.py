#LINk: https://leetcode.com/problems/valid-word/

# LeetCode 3136. Valid Word
# Time: O(n), Space: O(1)

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowels = has_cons = False

        for ch in word:
            if not ch.isalnum():
                return False 

            if ch.isalpha():
                if ch in vowels:
                    has_vowels = True
                else:
                    has_cons = True

        return has_vowels and has_cons
