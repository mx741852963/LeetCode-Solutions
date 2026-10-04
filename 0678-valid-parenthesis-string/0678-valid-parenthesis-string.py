class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        bal_r = 0
        bal_l = 0
        for i in range(n):
            j = n - i - 1
            if s[i]== "*" or s[i] == "(":
                bal_r += 1
            else:
                bal_r -= 1
            if  s[j]== "*"  or s[j] == ")":
                bal_l += 1
            else:
                bal_l -= 1
            if bal_l < 0 or bal_r < 0:
                return False
        return True
# Time O(N)
# Spcae O(1)