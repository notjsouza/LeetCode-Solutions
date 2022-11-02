class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}
        l = 0
        longest = 0
        
        for r in range(len(s)):
            
            if not s[r] in d: longest = max(longest, (r - l) + 1)
            else:
                
                if d[s[r]] < l: longest = max(longest, (r - l) + 1)
                else: l = d[s[r]] + 1
            
            d[s[r]] = r
        
        return longest
