class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        j, out = 0, 0

        for i in range(len(s)):
            while s[i] in set1:
                set1.remove(s[j])
                j+=1
            set1.add(s[i])
            out = max(out, (i-j+1))

        return out
