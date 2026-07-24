class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
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