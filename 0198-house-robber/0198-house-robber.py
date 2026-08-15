class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top Down
        # Time and Space O(n)
        # n = len(nums)
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])
        #     return max(nums[i] + dfs(i - 2), dfs(i - 1))

        # return dfs(n - 1)

        # Bottom UP
        # Time and Space O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]
