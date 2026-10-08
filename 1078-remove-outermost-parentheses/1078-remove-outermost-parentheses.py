class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        bal = 0
        for char in s:
            if char == ")":
                bal -= 1
            if bal > 0:
                ans.append(char)
            if char == "(":
                bal += 1
        return "".join(ans)
