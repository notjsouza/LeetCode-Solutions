class Solution:
    def reverseWords(self, s: str) -> str:
        str = s.split(' ')
        str.reverse()
        out = ""
        for n in str:
            if n != '':
                out += n + ' '
        return out[:-1]
