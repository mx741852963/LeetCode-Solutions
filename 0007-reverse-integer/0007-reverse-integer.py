class Solution:
    def reverse(self, x: int) -> int:
        max_int = (pow(2, 31) - 1) // 10
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > max_int or (rev == max_int) and pop > 7:
                return 0
            rev = rev * 10 + pop
        return rev * sign
# Time O(log10(n))
# Space O(1)
