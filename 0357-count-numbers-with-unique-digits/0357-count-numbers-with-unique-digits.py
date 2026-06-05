class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        arr = [9] * n  
        @cache
        def dp(i, tight, mask, is_actual):
            if i == n:
                return 1
            mx = arr[i] if tight else 9
            res = 0
            for d in range(mx + 1):
                if is_actual and (mask & (1 << d)):
                    continue 
                ntight = tight and (d == mx)
                next_is_actual = is_actual or (d > 0)
                if next_is_actual:
                    next_mask = mask | (1 << d)
                else:
                    next_mask = mask
                res += dp(i + 1, ntight, next_mask, next_is_actual)           
            return res
        return dp(0, True, 0, False)