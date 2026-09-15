class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if len(s) == 1:
            return 1
        self.count = 0
        self.last_end = -1

        def expand(l, r):
            while l > self.last_end and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    self.count += 1
                    self.last_end = r
                    return True
                l -= 1
                r += 1
            return False

        for i in range(n):
            if not expand(i, i):
                expand(i, i + 1)
        return self.count
