class Solution:
    def decodeString(self, s: str) -> str:
        stack, cur, num = [], "", 0
        for char in s:
            match char:
                case "[":
                    stack.append((cur, num))
                    cur, num = "", 0
                case "]":
                    prev, prev_num = stack.pop()
                    cur = prev + (cur * prev_num)
                case _ if char.isdigit():
                    num = num * 10 + int(char)
                case _:
                    cur += char

        return cur
# Time and Space O(N)