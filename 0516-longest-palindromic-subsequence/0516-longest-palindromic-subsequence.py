class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Bottom up Dp (tabulation)
        text1 = s
        text2 = s[::-1]
        n  = len(text1)
        if text1 == text2:
            return len(text1)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            prev = 0
            for j in range(1,n+1):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] =prev +1
                else:
                    dp[j] = max( dp[j-1], dp[j])
                prev = temp
        return dp[-1]
# Time O(n^2)
# Space O(n)