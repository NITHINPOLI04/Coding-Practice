#LINk: https://leetcode.com/problems/happy-number/

# LeetCode 202. Happy Number
# Time: O(logn), Space: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            current = n
            while current > 0:
                digit = current % 10
                total += digit * digit
                current //= 10
            n = total

        return n == 1
