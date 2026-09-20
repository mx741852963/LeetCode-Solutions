class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((123- ord(char)) * i for i, char in enumerate(s, 1))
        # Time O(n)
        # Space O(1)
