class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            match char:
                case "#":
                    res.extend(res)
                case "%":
                    res = res[::-1]
                case "*":
                    res = res[:-1]
                case _:
                    res.append(char)
        return ''.join(res)