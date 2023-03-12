class Solution:
    def romanToInt(self, s: str) -> int:
        i, out = 0, 0
        while i < len(s):
            cur = s[i:i+2]
            if cur[:1] == 'I':
                if cur[1:] == 'V': 
                    out += 4
                    i += 1
                elif cur[1:] == 'X': 
                    out += 9
                    i += 1
                else: out += 1
            elif cur[:1] == 'X':
                if cur[1:] == 'L': 
                    out += 40
                    i += 1
                elif cur[1:] == 'C': 
                    out += 90
                    i += 1
                else: out += 10
            elif cur[:1] == 'C':
                if cur[1:] == 'D': 
                    out += 400
                    i += 1
                elif cur[1:] == 'M': 
                    out += 900
                    i += 1
                else: out += 100
            elif cur[:1] == 'V': out += 5
            elif cur[:1] == 'L': out += 50
            elif cur[:1] == 'D': out += 500
            else: out += 1000
            i += 1
        return out
