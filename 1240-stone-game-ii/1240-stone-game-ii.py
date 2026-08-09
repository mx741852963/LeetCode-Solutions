class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = list(accumulate(piles[::-1]))[::-1]

        @cache
        def backtrack(i, M):
            if i >= n:
                return 0
            if n - i <= 2 * M:
                return suffix_sum[i]
            max_alice_score = 0

            for X in range(1, 2 * M + 1):
                next_M = max(M, X)
                next_i = i + X
                opponent_score = backtrack(next_i, next_M)
                current_alice_score = suffix_sum[i] - opponent_score
                max_alice_score = max(max_alice_score, current_alice_score)
            return max_alice_score

        return backtrack(0, 1)
