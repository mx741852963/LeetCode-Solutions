class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if len(s) == 1:
            return s

        start = 0
        max_len = 0

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(n):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            current_max = max(len1, len2)
            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2
        return s[start : start + max_len]


# Time  O(n^2)
# Space O(1)
