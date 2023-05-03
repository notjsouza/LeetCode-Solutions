class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        localMax, totalMax = 0, float('-inf')
        for n in nums:
            if n > (localMax + n):
                totalMax = max(totalMax, n)
                localMax = n
            else:
                localMax += n
                totalMax = max(totalMax, localMax)
        return totalMax
