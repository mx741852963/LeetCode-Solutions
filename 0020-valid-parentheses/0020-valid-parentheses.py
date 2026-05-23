from collections import Counter
class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stk = []
        for c in s:
            if c not in hashmap :
                stk.append(c)
            else:
                if not stk :
                    return False
                else:
                    if stk.pop() != hashmap[c]:
                        return False
        return not stk
# Time = O(n)
# Space = O(n)
