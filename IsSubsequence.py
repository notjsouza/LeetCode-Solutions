class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        sub = 0
        
        for i in t:
            
            if sub == len(s):
                
                return True
            
            if s[sub] == i:
                
                sub += 1
                
        return sub == len(s)
