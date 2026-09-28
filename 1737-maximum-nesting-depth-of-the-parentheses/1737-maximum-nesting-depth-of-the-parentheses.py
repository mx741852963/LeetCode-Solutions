class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = cur_depth = 0
        for char in s:
            match char:
                case "(":
                    cur_depth += 1
                    max_depth = max(max_depth, cur_depth)
                case ")":
                    cur_depth -= 1

        return max_depth


# Time O(N) Space O(1)
