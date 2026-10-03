class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        r = l = 0
        max_sub = 0
        for i in range(n):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if r == l:
                max_sub = max(max_sub, r * 2)
            elif r > l:
                r = l = 0
        r = l = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if r == l:
                max_sub = max(max_sub, l * 2)
            elif l > r:
                r = l = 0
        return max_sub
