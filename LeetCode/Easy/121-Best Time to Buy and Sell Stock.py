#LINk: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# LeetCode 121. Best Time to Buy and Sell Stock
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > best_buy:
                max_profit = max(max_profit, prices[i] - best_buy)
            
            best_buy = min(best_buy, prices[i])

        return max_profit
