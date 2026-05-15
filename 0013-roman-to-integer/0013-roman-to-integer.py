class Solution:
    def romanToInt(self, s: str) -> int:
        dictt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lenn = len(s)
        summ = 0
        i = 0
        while i < lenn:
            if i < lenn - 1 and dictt[s[i]] < dictt[s[i + 1]]:
                summ += dictt[s[i + 1]] - dictt[s[i]]
                i += 2
            else:
                summ += dictt[s[i]]
                i += 1
        return summ
# Time O(n)
# Space O(1)
                          
