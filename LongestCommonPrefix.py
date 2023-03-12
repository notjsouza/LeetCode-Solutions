class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub = ""
        for i in range(len(strs[0])):
            cur = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != cur: return sub
            sub += cur
        return sub
