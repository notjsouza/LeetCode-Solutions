class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left <= right:
            
            i = left + (right - left)//2
            if nums[i] == target: return i
            
            if nums[i] < target: left = i + 1
            else: right = i - 1

        return -1
