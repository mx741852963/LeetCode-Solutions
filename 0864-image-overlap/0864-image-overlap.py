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
        over_lap = 0
        shift_count = defaultdict(int)
        for r1, c1 in one1:
            for r2, c2 in one2:
                shift = (r2 - r1, c2 - c1)
                shift_count[shift] += 1
                over_lap = max(over_lap, shift_count[shift])
        return over_lap
