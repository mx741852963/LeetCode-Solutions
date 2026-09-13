class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        m = len(img1)
        n = len(img1[0])
        one1 = []
        one2 = []
        for r in range(m):
            for c in range(n):
                if img1[r][c] == 1:
                    one1.append((r, c))
                if img2[r][c] == 1:
                    one2.append((r, c))
        count = Counter((r-r0,c-c0)for r0,c0 in one1 for r,c in one2)
        return max(count.values()) if count else 0
