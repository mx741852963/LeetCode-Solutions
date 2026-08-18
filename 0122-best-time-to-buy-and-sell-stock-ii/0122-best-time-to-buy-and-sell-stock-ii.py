class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # res, s, p, i = 0, 0, 0, 0
        # while i < n - 1:
        #     while i < n - 1 and prices[i] >= prices[i + 1]:
        #         i += 1
        #     p = prices[i]
        #     while i < n - 1 and prices[i] <= prices[i + 1]:
        #         i += 1
        #     s = prices[i]
        #     res += s - p
        # return res
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res


# Time O(n)
# Spcae O(1)
