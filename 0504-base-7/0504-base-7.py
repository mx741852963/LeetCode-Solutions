class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        num = abs(num)
        res = ""
        while num:
            res = str(num % 7) + res
            num = num // 7

        return sign + res
    # Time and Space O(n)