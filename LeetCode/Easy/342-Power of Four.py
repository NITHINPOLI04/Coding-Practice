#LINk: https://leetcode.com/problems/power-of-four/

# LeetCode 342. Power of Four
# Time: O(logN), Space: O(1)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return n == 1
