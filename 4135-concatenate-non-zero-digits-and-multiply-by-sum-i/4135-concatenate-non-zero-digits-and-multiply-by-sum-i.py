class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        res, sol = 0, ""
        while n:
            tem = n % 10
            if tem > 0:
                sol += "".join(str(tem))
            res += tem
            n = n // 10
        return res * int(sol[::-1])
