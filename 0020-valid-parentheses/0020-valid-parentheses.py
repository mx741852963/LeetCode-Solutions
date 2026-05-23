class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(','}':'{',']':'['}
        stk = []
        if len(s) & 1:
            return False
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
