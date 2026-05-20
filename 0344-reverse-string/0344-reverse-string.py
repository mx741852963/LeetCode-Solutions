class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]
        # i = 0
        # j = len(s) - 1
        # k = 0
        # while k < len(s) // 2:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        #     k += 1
    # Time O(n)
    # Space O(1)