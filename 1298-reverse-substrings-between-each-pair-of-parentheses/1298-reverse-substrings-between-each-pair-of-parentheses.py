class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, cur = [], []
        for char in s:
            match char:
                case "(":
                    stack.append(cur)
                    cur = []
                case ")":
                    cur = stack.pop() + cur[::-1]
                case _:
                    cur.append(char)


        return "".join(cur)
