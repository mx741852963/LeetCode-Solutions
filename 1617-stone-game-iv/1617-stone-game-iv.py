class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def backtrack(i):
            if i == 0:
                return False
            if i == 1:
                return True
            for j in range(floor(sqrt(i)), 0, -1):
                if not backtrack(i - j**2):
                    return True
            return False
        return backtrack(n)
