class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        sett = set()
        for i in word :
            if i.islower() and i.upper() in word :
                sett.add(i)
        return len(sett)