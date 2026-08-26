class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        h = []
        min_len = len(s) +1 
        for i in range(len(s)):
            if s[i] == "1":
                h.append(i)
        if len(h) < k:
            return ""
        for j in range(len(h) - k + 1):
            sub = s[h[j] : h[j + k - 1] + 1]
            if len(sub) < min_len:
                ans = sub
                min_len = len(sub)
            elif len(sub) == min_len:
                ans = min(ans, sub)
        return ans
