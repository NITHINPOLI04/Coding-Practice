#LINk: https://leetcode.com/problems/h-index/

# LeetCode 274. H-Index
# Approach 1: Using Extra Variable h
# Time: O(n), Space: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        return h

------------------------------------------------------

# Approach 2: Without using any Extra Variable 
# Time: O(nlogn), Space: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)
