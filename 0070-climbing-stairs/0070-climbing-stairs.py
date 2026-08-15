class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def backtrack(i):
            if i == n:
                return 1
            if i > n:
                return 0
            return backtrack(i + 1) + backtrack(i + 2)
        return backtrack(0)
