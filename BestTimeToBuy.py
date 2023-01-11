class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest, maxProfit = prices[0], 0
        
        for num in prices:
            
            if num < lowest: lowest = num
            maxProfit = max(maxProfit, num - lowest)
            
        return maxProfit
