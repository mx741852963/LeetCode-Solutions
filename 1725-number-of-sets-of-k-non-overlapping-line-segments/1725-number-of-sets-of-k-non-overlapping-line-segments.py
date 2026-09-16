class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n+k-1,k*2)%(10**9+7)
        # Time O(min(n+k-1,k*2))
        # Space O(1)
        # mod = 10**9 + 7
        # @cache
        # def dp(i, seg, first):
        #     if seg == 0:
        #         return 1
        #     if i == n:
        #         return 0
        #     res = dp(i+1, seg, first)
        #     if first:
        #         res += dp(i + 1, seg, False)
        #     else:
        #         res += dp(i, seg - 1, True)
        #     return res % mod

        # return dp(0, k, True)
        # Time and Space O(nk)

