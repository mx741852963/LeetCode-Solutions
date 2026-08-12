class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(n):
            counter[nums[r]] += 1
            while counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len


# Time and Space O(n)
