#LINk: https://leetcode.com/problems/find-words-containing-character/

# LeetCode 2942. Find Words Containing Character
# Time: O(n), Space: O(1)

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []

        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        
        return result
