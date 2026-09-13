class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m, n = len(img1), len(img1[0])
        one1 = [(r, c) for r in range(m) for c in range(n) if img1[r][c] == 1]
        one2 = [(r, c) for r in range(m) for c in range(n) if img2[r][c] == 1]
        count = Counter((r - r0, c - c0) for r0, c0 in one1 for r, c in one2)
        return max(count.values()) if count else 0
# Time O(n**4) Space O(n**2)