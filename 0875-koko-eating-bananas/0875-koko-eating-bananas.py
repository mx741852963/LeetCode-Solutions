class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def dose_k(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h
        if len(piles) == 1 and piles[0]==h :
            return piles[0]
        if len(piles) == h:
            return max(piles)
        # l = ceil(sum(piles)/h)
        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2
            if dose_k(k):
                r = k
            else:
                l = k + 1
        return r
