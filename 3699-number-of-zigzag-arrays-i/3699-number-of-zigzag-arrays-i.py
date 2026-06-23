class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # mod = 10 ** 9 + 7
        # m = r - l + 1
        # dp = [1] * m       
        # for _ in range(n - 1):
        #     sum_dp = list(itertools.accumulate(dp, initial=0))
        #     x = sum_dp[-1]
        #     dp = [(x - sum_dp[m - i]) % mod for i in range(m)]          
        # return (sum(dp) * 2) % mod
        # mod = 10 ** 9 + 7
        # m = r - l + 1
        # dp_0 = [1] * m
        # dp_1 = [1] * m
        # for _ in range(n - 1):
        #     sum_0 = list(itertools.accumulate(dp_0, initial=0))
        #     sum_1 = list(itertools.accumulate(dp_1, initial=0))
        #     dp_0 = [num%mod for num in sum_1[:-1]]
        #     x = sum_0[-1]
        #     dp_1 = [(x-num) % mod for num in sum_0[1:]]
        # return (sum(dp_1) + sum(dp_0))%mod  
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