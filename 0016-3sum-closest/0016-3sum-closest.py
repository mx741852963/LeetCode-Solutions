class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_target = float("inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[hi] + nums[lo]
                if abs(cur_sum - target) < abs(closest_target - target):
                    closest_target = cur_sum
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1
        return closest_target
