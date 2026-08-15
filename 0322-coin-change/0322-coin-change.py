class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        @cache
        def min_coins(amt):
            if amt == 0: return 0
            minn = float("inf")
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minn = min(minn,1+min_coins(diff))
            return minn
        res = min_coins(amount)
        if res < float("inf"):
            return res
        else :
            return -1