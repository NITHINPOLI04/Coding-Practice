#LINk: https://leetcode.com/problems/find-lucky-integer-in-an-array/

# LeetCode 1394. Find Lucky Integer in an Array
# Time: O(n), Space: O(n)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        max_lucky = -1
        for num,freq in count.items():
            if num == freq:
                max_lucky = max(max_lucky, num)
        
        return max_lucky
