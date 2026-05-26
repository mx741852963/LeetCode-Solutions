class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # sett = set()
        # for i in word :
        #     if i.islower() and i.upper() in word :
        #         sett.add(i)
        # return len(sett)
        # # Time O(n)
        # # space O(1)
        sett = set()
        [sett.add(i) for i in word  if i.islower() and i.upper() in word]
        return len(sett)