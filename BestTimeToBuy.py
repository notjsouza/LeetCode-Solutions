class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        maxProfit = 0
        
        for num in prices:
            
            if num < lowest: lowest = num
            maxProfit = max(maxProfit, num - lowest)
            
        return maxProfit
