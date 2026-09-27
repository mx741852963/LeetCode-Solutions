class Solution:
    def calculate(self, s: str) -> int:
        stack, cur, sign, res = [], 0, 1, 0
        for char in s:
            match char:
                case "(":
                    stack.append((res, sign))
                    res, sign = 0, 1
                case ")":
                    res += sign * cur
                    cur = 0
                    prev, sign = stack.pop()
                    res = prev + (res * sign)
                case "+":
                    res += sign * cur
                    cur = 0
                    sign = 1
                case "-":
                    res += sign * cur
                    cur = 0
                    sign = -1
                case " ":
                    continue
                case _:
                    cur = cur * 10 + int(char)

        return res + (sign * cur)
# Time and Space O(N)


# Time and Space O(N)
