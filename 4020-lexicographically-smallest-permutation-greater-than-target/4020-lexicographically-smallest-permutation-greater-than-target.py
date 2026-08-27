class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        sol, n = [], len(s)
        s = sorted(s)
        visited = set()

        def backtrack():
            if len(sol) == n:
                ss = "".join(sol[:])
                return ss if ss > target else ""
            curr_len = len(sol)
            for i in range(n):
                if i not in visited:
                    char = s[i]
                    if i > 0 and s[i] == s[i - 1] and (i - 1) not in visited:
                        continue
                    temp_prefix = "".join(sol) + char
                    if temp_prefix < target[: curr_len + 1]:
                        continue

                    visited.add(i)
                    sol.append(char)
                    res = backtrack()
                    if res:
                        return res
                    sol.pop()
                    visited.remove(i)
        return backtrack() if  backtrack() else ""
