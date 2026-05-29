class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0]*26  
        l = 0
        maxx = 0
        lenn = len(s)
        for r in range(lenn):
            count[ord(s[r])-65]  += 1
            while (r - l + 1) - max(count) > k :
                count[ord(s[l])-65] -= 1
                l += 1
            maxx = max(maxx, (r - l + 1))
        return maxx