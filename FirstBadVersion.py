class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 0
        right = n
        
        while left <= right:
            
            m = left + (right - left)//2
            
            if isBadVersion(m): right = m-1
            else: left = m + 1
                
        if right < m: return m
        if left > m: return m + 1
        return -1
