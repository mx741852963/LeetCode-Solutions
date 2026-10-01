class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in s:
            match char:
                case "(" | "[" | "{":
                    stack.append(char)
                case _:
                    if not stack or stack.pop() != pairs[char]:
                        return False
        return not stack


# Time and Space O(N)
