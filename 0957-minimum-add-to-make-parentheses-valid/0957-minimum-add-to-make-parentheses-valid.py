class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        nd = bal = 0
        for char in s:
            if char == "(":
                bal += 1
            else:
                if bal > 0:
                    bal -= 1
                else:
                    nd += 1
        return bal + nd


# Time O(N)
# Space O(n)
