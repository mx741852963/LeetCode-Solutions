class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        bal = [0, 0]
        if n & 1:
            return False
        for i in range(n):
            j = n - i - 1
            if locked[i] == "0" or s[i] == "(":
                bal[0] += 1
            else:
                bal[0] -= 1
            if locked[j] == "0" or s[j] == ")":
                bal[1] += 1
            else:
                bal[1] -= 1
            if bal[0] < 0 or bal[1] < 0:
                return False
        return True
