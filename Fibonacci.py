class Solution:
    def fib(self, n: int) -> int:

        arr = [0, 1]

        for i in range(1, n):

            arr.append(arr[i] + arr[i-1])

        return arr[n]
