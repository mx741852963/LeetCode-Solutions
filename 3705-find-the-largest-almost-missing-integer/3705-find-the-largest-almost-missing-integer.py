class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        n = len(nums)
        if k == n:
            return max(nums)
        unique = []
        for num, vreq in counter.items():
            if vreq == 1:
                unique.append(num)
        if k == 1:
            return max(unique) if unique else -1
        return max(
            nums[0] if counter[nums[0]] == 1 else -1,
            nums[-1] if counter[nums[-1]] == 1 else -1,
        )
