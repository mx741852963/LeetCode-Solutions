class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack,groups,cur= [],[],{""}
        for char in expression:
            match char:
                case "{":
                    stack.append((groups, cur))
                    groups, cur = [], {""}
                case ",":
                    groups.append(cur)
                    cur = {""}
                case "}":
                    word_set = set().union(*groups, cur)
                    prev_groups, prev_cur = stack.pop()
                    cur,groups = {a + b for a in prev_cur for b in word_set},prev_groups
                case _:
                    cur = {a + char for a in cur}
        return sorted(list( set().union(*groups, cur)))
# Time O(n*k)
# Space O(k)