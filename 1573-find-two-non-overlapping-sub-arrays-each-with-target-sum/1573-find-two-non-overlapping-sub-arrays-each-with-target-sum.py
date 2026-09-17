class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        l = 0
        dp = [inf] * n
        cur_sum = 0
        ans =best_len= inf
        for r in range(n):
            cur_sum += arr[r]
            while cur_sum > target:
                cur_sum -= arr[l]
                l += 1
            if cur_sum == target:
                ans = min(ans, r - l + 1 + (dp[l - 1]if l > 0 and dp[l - 1] != inf else inf ))
                best_len = min(best_len, r - l + 1)
            dp[r] = min(dp[r - 1] if r > 0 else inf, best_len)
        return ans if ans != inf else -1
# Time and Space O(n)
