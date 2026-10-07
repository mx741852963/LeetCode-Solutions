class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        ans = []
        self.maxx = -1

        @cache
        def backtrack(i, curr, bal):
            if bal < 0:
                return
            if i == n:
                if bal == 0:
                    curr_len = len(curr)
                    if curr_len > self.maxx:
                        self.maxx = curr_len
                        ans.append(curr)
                    elif self.maxx == curr_len:
                        ans.append(curr)
                return
            char = s[i]
            if char not in "()":
                backtrack(i + 1, curr + char, bal)
            else:
                backtrack(i + 1, curr + char, bal + (1 if char == "(" else -1))
                backtrack(i + 1, curr, bal)

        backtrack(0, "", 0)
        return ans if ans else [""]


# Time O(2**n)
# Space O(n)
