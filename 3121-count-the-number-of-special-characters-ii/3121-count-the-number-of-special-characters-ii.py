from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        lower = defaultdict(list)
        upper = defaultdict(list)
        for i in range(len(word)):
            if word[i].islower():
                lower[word[i]].append(i)
            else:
                upper[word[i]].append(i)
        for i in lower:
            j = i.upper()
            if j in upper and max(lower[i]) < min(upper[j]) :
                count += 1
        count
        return count