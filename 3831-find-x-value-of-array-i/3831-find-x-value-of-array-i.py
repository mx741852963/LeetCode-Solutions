class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            n_dp = [0] * k
            n_dp[num % k] = 1
            for r in range(k):
                if dp[r] == 0:
                    continue
                n_dp[(r * num) % k] += dp[r]
            dp = n_dp
            for r in range(k):
                ans[r] += dp[r]
        return ans


# Time and Space O(n*k)
