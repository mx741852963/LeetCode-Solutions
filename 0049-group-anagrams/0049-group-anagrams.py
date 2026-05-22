from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for str_ in strs:
            listt = [0] * 26
            for char in str_:
                listt[ord(char) - 97] += 1
            tuplee = tuple(listt)
            counter[tuplee].append(str_)
        return list(counter.values())
# Time O(n*m)
# Space O(n*m)