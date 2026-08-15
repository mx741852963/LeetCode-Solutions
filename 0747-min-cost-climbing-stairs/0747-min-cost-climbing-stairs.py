class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n  = len(cost)
        @cache
        def min_cost(i):
            if i <  2 :
                return 0
            return min(cost[i-2]+min_cost(i-2),cost[i-1]+min_cost(i-1))
        return min_cost(n)