import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1 and piles[0] == h:
            return piles[0]
        if len(piles) == h:
            return max(piles)
        l = math.ceil(sum(piles) / h)
        r = max(piles)
        c = math.ceil
        while l < r:
            k = (l + r) // 2
            if sum(c(p / k) for p in piles) <= h:
                r = k
            else:
                l = k + 1
        return r
