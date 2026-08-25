class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sett = set(nums)
        s = k
        while True:
            if k not in sett:
                return k
            else:
                k += s
