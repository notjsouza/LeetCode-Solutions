class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, cur = 0, len(height)-1, 0
        while l < r:
            cur = max(cur, (r - l) * min(height[r], height[l]))
            if height[r] < height[l]: r -= 1
            else: l += 1
        return cur
