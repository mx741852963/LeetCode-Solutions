class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        m = n
        for i in range(10):
            if m >= 10:
                if n <= m and (m % 10) * (m // 10) % t == 0:
                    return m
            elif m < 10:
                if n <= m and m % t == 0:
                    return m
            m += 1
# Time and Spcae O(1)