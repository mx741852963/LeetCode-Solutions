class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l = 0
        x = float("inf")
        dp = [x] * n
        cur_sum = 0
        ans =best_len= x
        for r in range(n):
            cur_sum += arr[r]
            while cur_sum > target:
                cur_sum -= arr[l]
                l += 1
            if cur_sum == target:
                if l > 0 and dp[l - 1] != x:
                    ans = min(ans, r - l + 1 + dp[l - 1])
                best_len = min(best_len, r - l + 1)
            dp[r] = min(dp[r - 1] if r > 0 else x, best_len)
        return ans if ans != x else -1
