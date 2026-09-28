class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = -1
        r_p = 0
        l_p = 0
        for char in s:
            match char:
                case ")":
                    r_p += 1
                case "(":
                    l_p += 1
            max_depth = max(max_depth, l_p - r_p)
        return max_depth
# Time O(N) Space O(1)