class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ = set(nums)
        maxx = 0
        for i in nums_:
            if i - 1 not in nums_:
                next_num = i + 1
                count = 1
                while next_num in nums_:
                    count += 1
                    next_num += 1
                maxx = max(maxx, count)
        return maxx