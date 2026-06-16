class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            match char:
                case "#":res.extend(res)
                case "%":res.reverse()
                case "*":
                    if res:res.pop()
                case _:res.append(char)
        return ''.join(res)
# Time O(n)
# Space O(n)