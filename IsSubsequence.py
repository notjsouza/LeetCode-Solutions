class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        for char in t: 
            
            if s and char == s[0]: s = s[1:]
        
        return True if not s else False
