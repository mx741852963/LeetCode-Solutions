class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, sol = [], []
        n = len(s)

        def backtrack(start_idx):
            if len(sol) == 4:
                if start_idx == n:
                    res.append(".".join(sol))
                return
            for end_idx in range(start_idx + 1, min(start_idx + 4, n + 1)):
                part = s[start_idx:end_idx]
                if part.startswith("0") and len(part) > 1:
                    continue
                if int(part) > 255:
                    continue
                sol.append(part)
                backtrack(end_idx)
                sol.pop()

        backtrack(0)
        return res
# Time O(1) or O(3**4)
# Space O(1)
