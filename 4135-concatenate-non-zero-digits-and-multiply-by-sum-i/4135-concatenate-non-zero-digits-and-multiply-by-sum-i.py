class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        res, sol, place = 0, 0, 1
        while n:
            tem = n % 10
            if tem > 0:
                sol = sol + (tem * place)
                place *= 10
            res += tem
            n = n // 10
        return res * sol


# Time O(D)
#  Space O(1)
