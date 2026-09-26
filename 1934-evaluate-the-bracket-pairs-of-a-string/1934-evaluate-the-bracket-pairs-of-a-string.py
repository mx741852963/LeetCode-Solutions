class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hash = {k: v for k, v in knowledge}
        res, i, n = [], 0, len(s)
        while i < n:
            if s[i] == "(":
                i += 1
                start = i
                while s[i] != ")":
                    i += 1
                res.append(hash.get(s[start:i], "?"))
            else:
                res.append(s[i])
            i += 1
        return "".join(res)


# Time and Space O(N+M)
