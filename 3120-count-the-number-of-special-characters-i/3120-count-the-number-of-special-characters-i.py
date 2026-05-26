class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sett = set(word)
        count = 0
        for i in sett:
            if i.islower() and i.upper() in sett:
                count += 1
        return count
        # # Time O(n)
        # # space O(1)
