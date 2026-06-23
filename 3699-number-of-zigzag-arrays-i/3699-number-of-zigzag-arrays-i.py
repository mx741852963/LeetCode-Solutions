class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int: 
        mod = 10 ** 9 + 7
        m = r - l + 1       
        if m == 1:
            return 1 if n == 1 else 0           
        dp = [1] * m        
        for _ in range(n - 1):
            new_dp = [0] * m
            running_sum = 0
            for i in range(m - 1, 0, -1):
                running_sum = (running_sum + dp[i]) % mod
                new_dp[m - i] = running_sum      
            dp = new_dp
        return (sum(dp) * 2) % mod