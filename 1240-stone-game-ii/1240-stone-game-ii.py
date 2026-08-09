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
            return max(
                suffix_sum[i] - backtrack(i + X, max(M, X)) for X in range(1, 2 * M + 1)
            )

        return backtrack(0, 1)


# Time O(n*3) Space O(n*2)
