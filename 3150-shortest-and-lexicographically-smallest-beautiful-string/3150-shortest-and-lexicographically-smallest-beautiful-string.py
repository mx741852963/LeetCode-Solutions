class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        h = []
        n = len(s)
        min_len = n + 1
        for i in range(n):
            if s[i] == "1":
                h.append(i)
        hh = len(h)
        if hh < k:
            return ""
        for j in range(hh - k + 1):
            sub = s[h[j] : h[j + k - 1] + 1]
            if len(sub) < min_len:
                ans = sub
                min_len = len(sub)
            elif len(sub) == min_len:
                ans = min(ans, sub)
        return ans
#  Time and Space O(n)