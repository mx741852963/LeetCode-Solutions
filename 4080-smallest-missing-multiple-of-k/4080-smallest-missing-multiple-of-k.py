class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sett = set(nums)
        multiple = k
        while multiple in sett:
            multiple += k
        return multiple
        # Time O(n) Space O(n)
