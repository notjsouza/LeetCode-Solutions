class Solution:
    def rob(self, nums: List[int]) -> int:
        
        house1 = house2 = 0
        
        for house in nums:
            
            temp = max(house1 + house, house2)
            house1 = house2
            house2 = temp
            
        return house2
