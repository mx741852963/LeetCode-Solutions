class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # mp = list(accumulate(nums))
        count = 0
        mp = {0: 1}
        prefix = 0
        for num in nums:
            prefix += num
            if prefix - k in mp:
                count += mp[prefix - k]
            mp[prefix] = mp.get(prefix, 0) + 1
        return count
