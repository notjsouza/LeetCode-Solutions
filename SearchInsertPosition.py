class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            n = l + (r - l) // 2
            if nums[n] == target: return n
            elif nums[n] < target: l = n + 1
            else: r = n - 1
                
        return l
