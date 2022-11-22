class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        points, pre, cur = Counter(nums), 0, 0
        for val in range(max(points.keys()) + 1): pre, cur = cur, max(pre + val * points[val], cur)
        return cur
