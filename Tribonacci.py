class Solution:
    def tribonacci(self, n: int) -> int:
        
        d = [0, 1, 1]
        
        for i in range(n-1): d.append(d[i] + d[i+1] + d[i+2])
            
        return d[n]
