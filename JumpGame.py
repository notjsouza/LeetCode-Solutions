class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end = len(nums)-1
        for i, cur in reversed(list(enumerate(nums))):
            
            if i + cur >= end: end = i
        
        if end == 0: return True
        return False
