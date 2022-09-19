class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = 0
        maxCur = float('-inf')
        
        for num in nums:
            
            if num > (cur + num):
                
                maxCur = max(maxCur, num)
                cur = num
            
            else:
                
                cur += num
                maxCur = max(maxCur, cur)
                
        return maxCur
