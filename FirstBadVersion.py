class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l, r = 0, n
        
        while l <= r:
            
            i = l + (r - l)//2
            
            if isBadVersion(i): r = i - 1
            else: l = i + 1
                
        if r < i: return i
        if l > i: return i + 1
        return -1
