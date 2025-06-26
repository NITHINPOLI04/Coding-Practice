#LINk: https://leetcode.com/problems/maximum-product-subarray/

# LeetCode 152. Maximum Product Subarray
# Time: O(n), Space: O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = max_product = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = curr_max

            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, temp_max * num, curr_min * num)

            max_product = max(max_product, curr_max)

        return max_product
