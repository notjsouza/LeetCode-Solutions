class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points, pre, cur = [0] * 10001, 0, 0
        
        for num in nums: points[num] += num
        for val in points: pre, cur = cur, max(pre + val, cur)
            
        return cur
