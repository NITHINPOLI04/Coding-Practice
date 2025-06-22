#LINk: https://leetcode.com/problems/maximum-subarray/

# LeetCode 53. Maximum Subarray
# Time: O(n), Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = float('-inf')
        for i in nums:
            currsum = currsum + i
            maxsum = max(currsum, maxsum)
            if currsum < 0:
                currsum = 0
        return maxsum
