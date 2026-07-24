class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # Top Down DP (Memoization)
        # m ,n  = len(text1),len(text2)
        # # Time and Space O(m*n)
        # @cache
        # def lcs(i,j):
        #     if i == m or j == n: return 0
        #     elif text1[i]==text2[j]:
        #         return 1 + lcs(i+1,j+1)
        #     else :
        #         return max(lcs(i+1,j),lcs(i,j+1))
        # return lcs(0,0)

        # Bottom up Dp (tabulation)

        m ,n  = len(text1),len(text2)
        if text1 == text2:
            return len(text1)
        texts = set(text1) & set(text2)
        if len(texts) == 0:
            return 0
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        dp = [0]*(n+1)
        for i in range(1,m+1):
            prev = 0
            for j in range(1,n+1):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] =prev +1
                else:
                    dp[j] = max( dp[j-1], dp[j])
                prev = temp
        return dp[-1]
# Time O(n*m) Space O(min(m,n))
