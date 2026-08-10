class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def backtrack(i):
            if i == 0:
                return False
            k = 1
            while k * k <= i:
                if not backtrack(i - k * k):
                    return True
                k += 1
            return False

        return backtrack(n)
