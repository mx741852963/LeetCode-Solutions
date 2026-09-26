class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hash = defaultdict(str)
        for key, val in knowledge:
            hash[f"({key})"] = val
        i = 0
        n = len(s)
        ans = s
        while i < n:
            if s[i] == "(":
                sub = ""
                while s[i] != ")":
                    sub += s[i]
                    i += 1
                sub += ")"
                if hash[sub]:
                    ans = ans.replace(sub, hash[sub])
                else:
                    ans = ans.replace(sub, "?")
            i += 1
        return ans
