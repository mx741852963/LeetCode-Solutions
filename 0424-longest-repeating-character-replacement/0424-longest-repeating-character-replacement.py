class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26  
        l = 0
        lenn = len(s)
        max_freq = 0  
        for r in range(lenn):
            idx = ord(s[r]) - 65
            count[idx] += 1
            if count[idx] > max_freq:
                max_freq = count[idx]
            if (r - l + 1) - max_freq > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
        return lenn - l