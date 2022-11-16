class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        return max(self.maxRob(nums[1:]), self.maxRob(nums[:-1]))
    
    def maxRob(self, nums):
            
        house1 = house2 = 0
        
        for house in nums:
                
            house1, house2 = max(house1, house2 + house), house1
            
        return house1
