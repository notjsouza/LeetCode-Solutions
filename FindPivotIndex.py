class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)

        for i, num in enumerate(nums):
            if l == (r - l) - num: return i
            l += num

        return -1
