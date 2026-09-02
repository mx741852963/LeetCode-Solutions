class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums) - 1
        l = r = k
        max_sub = nums[k]
        cur_min = nums[k]
        while l > 0 or r < n:
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < n else 0
            if left > right:
                l -= 1
                cur_min = min(left, cur_min)
            else:
                r += 1
                cur_min = min(right, cur_min)
            max_sub = max(cur_min * (r - l + 1), max_sub)
        return max_sub


# Time O(n)
# Space O(1)
