from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)
        for i in magazine:
            counter[i] += 1
        for i in ransomNote:
            if i not in counter:
                return False
            elif counter[i]==1:
                del counter[i]
            else:
                counter[i] -= 1
        return True
# Time O(n+m)
# Space O(1)
     