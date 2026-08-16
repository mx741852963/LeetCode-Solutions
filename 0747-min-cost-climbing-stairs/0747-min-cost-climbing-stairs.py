class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top Down with memo
        # Time O(n)
        # Space O(n)
        # n  = len(cost)
        # @cache
        # def min_cost(i):
        #     if i <  2 :
        #         return 0
        #     return min(cost[i-2]+min_cost(i-2),cost[i-1]+min_cost(i-1))
        # return min_cost(n)

        # Botton up  DP (Tabulation)
        # Time O(n)
        # Space O(n)
        n  = len(cost)
        dp = [0] *(n+1)
        for i in range(2,n+1):
           dp[i]= min(cost[i-2]+dp[i-2],cost[i-1]+dp[i-1])
        return dp[-1]