class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p = 1
        s = 0
        nums = n
        while n:
            tem = n % 10
            n //= 10
            s += tem
            p *= tem
        if p + s == 0:
            return False
        return (nums % (p + s)) == 0


# Time O(log10n)
# Space O(1)
