class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0

        for i, num in enumerate(nums):
            if l == (r - l) - num: return i
            l += num
        
        return -1
