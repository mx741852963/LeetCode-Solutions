class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter={}
        for str_ in strs:
            listt = [0] * 26
            for char in str_:
                listt[ord(char) - 97] += 1
            tuplee = tuple(listt)
            if tuplee not in counter:
                counter[tuplee] = []
            counter[tuplee].append(str_)
            # counter[tuplee] = counter.get(tuplee, []) + [str_] 
            val = list(counter.values())
        return val
