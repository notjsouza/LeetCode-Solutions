class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_t = {}
        t_s = {}
        
        for s1, t1 in zip(s, t):
            
            if (s1 not in s_t) and (t1 not in t_s):
                
                s_t[s1] = t1
                t_s[t1] = s1
                
            elif s_t.get(s1) != t1 or t_s.get(t1) != s1: return False
        
        return True
