#LINk: https://leetcode.com/problems/koko-eating-bananas/

# LeetCode 875. Koko Eating Bananas
# Time: O(Mlogn), Space: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = left + (right - left) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/mid)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result
