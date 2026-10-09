class Solution:
    def minInsertions(self, s: str) -> int:
        bal = 0
        res = 0
        for char in s:
            if char == "(":
                bal += 2
                if bal & 1:
                    bal -= 1
                    res += 1
            else:
                bal -= 1
                if bal < 0:
                    bal = 1
                    res += 1
        return res + bal
# Time O(n)