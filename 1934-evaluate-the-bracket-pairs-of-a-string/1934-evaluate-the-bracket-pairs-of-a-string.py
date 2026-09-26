class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hash = {k: v for k, v in knowledge}
        res, i, n = [], 0, len(s)
        while i < n:
            if s[i] == "(":
                i += 1
                key = ""
                while s[i] != ")":
                    key += s[i]
                    i += 1
                print(key)
                res.append(hash.get(key, "?"))
            else:
                res.append(s[i])
            i += 1
        return "".join(res)


# Time and Space O(N+M)
