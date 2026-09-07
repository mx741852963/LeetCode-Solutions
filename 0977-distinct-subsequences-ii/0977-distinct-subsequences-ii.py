class Solution:
    def distinctSubseqII(self, s: str) -> int:
        last = {}
        dp = 1
        mod = 10**9 + 7
        for char in s:
            new_dp = (dp * 2 - last.get(char, 0)) % mod
            last[char] = dp
            dp = new_dp
        return (dp - 1) % mod
# Time O(n)
# Spcae O(1)