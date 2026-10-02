class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        bal_r = 0
        bal_l = 0
        if n & 1:
            return False
        for i in range(n):
            j = n - i - 1
            if locked[i] == "0" or s[i] == "(":
                bal_r += 1
            else:
                bal_r -= 1
            if locked[j] == "0" or s[j] == ")":
                bal_l += 1
            else:
                bal_l -= 1
            if bal_l < 0 or bal_r < 0:
                return False
        return True
# Time O(n)
# Space O(1)