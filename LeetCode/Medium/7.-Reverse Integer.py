#LINk: https://leetcode.com/problems/reverse-integer/

# LeetCode 7. Reverse Integer
# Time: O(n), Space: O(n)

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        reversed_x = int(str(abs(x))[::-1])

        result = sign * reversed_x

        if result < INT_MIN or result > INT_MAX:
            return 0
        return result
