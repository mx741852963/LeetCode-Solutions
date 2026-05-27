from collections import defaultdict
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # count = 0
        # lower = defaultdict(list)
        # upper = defaultdict(list)
        # for i in range(len(word)):
        #     if word[i].islower():
        #         lower[word[i]].append(i)
        #     else:
        #         upper[word[i]].append(i)
        # for i in lower:
        #     j = i.upper()
        #     if j in upper and max(lower[i]) < min(upper[j]) :
        #         count += 1
        # count
        # return count
        last_lower = {}
        first_upper = {}
        for index, char in enumerate(word):
            if char.islower():
                last_lower[char] = index
            else:
                if char not in first_upper:
                    first_upper[char] = index
        count = 0
        for char, last_low_idx in last_lower.items():
            up_char = char.upper()
            if up_char in first_upper and last_low_idx < first_upper[up_char]:
                count += 1
        return count