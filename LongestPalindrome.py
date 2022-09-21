class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        hashMap = {}
        
        for char in s:
            
            if not char in hashMap: hashMap[char] = 1
            else: hashMap[char] += 1
            
        longest = 0
        for c in hashMap:
        
            longest += hashMap[c]//2 * 2
            if longest%2 == 0 and hashMap[c]%2 == 1: longest += 1
        
        return longest
