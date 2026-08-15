class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #  # Top Down with memo
        # # Time O(coins + amount)
        # # Space O(amount)
        # coins.sort()
        # @cache
        # def min_coins(amt):
        #     if amt == 0: return 0
        #     minn = float("inf")
        #     for coin in coins:
        #         diff = amt - coin
        #         if diff < 0:
        #             break
        #         minn = min(minn,1+min_coins(diff))
        #     return minn
        # res = min_coins(amount)
        # if res < float("inf"):
        #     return res
        # else :
        #     return -1

        # Bottom Up
        # Time O(coins + amount)
        # Space O(amount)
        coins.sort()
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
