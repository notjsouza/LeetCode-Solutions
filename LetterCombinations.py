class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        combo = []
        
        def rec(i, cur):
            if i == len(digits):
                combo.append(cur)
            else:
                for c in d[digits[i]]: rec(i + 1, cur + c)
        
        rec(0, '')
        return combo
