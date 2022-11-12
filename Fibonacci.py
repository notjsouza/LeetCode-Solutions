class Solution:
    def fib(self, n: int) -> int:
        
        d = [0, 1]
        
        for i in range(n-1): d.append(d[i] + d[i+1])
            
        return d[n]
