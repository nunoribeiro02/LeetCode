class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while (r < len(prices)):
            if (prices[l] > prices[r]):
                l = r
                r += 1
                continue
            
            if (profit < prices[r] - prices[l]):
                profit = prices[r] - prices[l]

            r += 1

        return profit
    
"""
Space: O(1)
Time: O(n), iterate over the array once
"""