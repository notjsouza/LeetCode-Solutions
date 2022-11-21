class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return 0
        
        l, r = 0, nums[0]
        c = 1
        
        while r < len(nums)-1:
            
            c += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
            
        return c
