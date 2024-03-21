class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        
        while guess((r+l)//2) != 0:
            
            if guess((r+l)//2) == 1:
                l = ((r+l)//2) + 1
            else:
                r = ((r+l)//2) - 1
        
        return (r+l)//2
