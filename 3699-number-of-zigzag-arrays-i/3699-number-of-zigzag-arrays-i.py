class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int: 
        mod = 10 ** 9 + 7
        m = r - l + 1  
        dp = [1] * m      
        if m == 1:return 1 if n == 1 else 0                 
        for _ in range(n - 1):dp = [0] + [num % mod for num in itertools.accumulate(reversed(dp))][:-1]
        return (sum(dp) * 2) % mod
# Time O(n*m) Spcae O(n)
        