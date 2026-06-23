class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int: 
        mod = 10 ** 9 + 7
        m = r - l + 1       
        if m == 1:
            return 1 if n == 1 else 0           
        dp = [1] * m        
        for _ in range(n - 1):
            dp = [0] + [num % mod for num in itertools.accumulate(reversed(dp))][:-1]
        return (sum(dp) * 2) % mod