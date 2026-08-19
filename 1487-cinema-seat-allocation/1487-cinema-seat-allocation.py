class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(int)
        res = 0
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                reserved[r] |= 1 << (c - 2)

        for mask in reserved.values():
            if mask & 15 == 0 and mask & 240 == 0:
                res += 2
            elif (mask & 15 == 0) or (mask & 240 == 0) or (mask & 60 == 0):
                res += 1
        return res + (n - len(reserved)) * 2
