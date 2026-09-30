class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        cur_depth = 0
        ans = []
        for char in seq:
            match char:
                case "(":
                    cur_depth += 1
                    ans.append(cur_depth & 1)
                case ")":
                    ans.append(cur_depth & 1)
                    cur_depth -= 1
        return ans
# Time O(N)
# Space O(1)