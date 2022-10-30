class Solution:
    def reverseWords(self, s: str) -> str:
    
        words = s.split()
        
        for i, n in enumerate(words):
            
            words[i] = n[::-1]
            
        return " ".join(words)
