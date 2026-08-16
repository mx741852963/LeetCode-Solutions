class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0 = c1 = c2 = 0
        for i in stones:
            val = i % 3
            if val == 0:
                c0 += 1
            elif val == 1:
                c1 += 1
            else:
                c2 += 1
        if c0 % 2 == 0:
            return c2 >= 1 and c1 >= 1
        return abs(c2 - c1) > 2


# Time O(n)
# Spcae O(1)
