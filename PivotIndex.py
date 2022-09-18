class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        lTotal = 0
        total = sum(nums)
        
        for i, n in enumerate(nums):
            
            if lTotal == (total - lTotal) - n:
                
                return i
            
            lTotal += n
        
        return -1
