class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)
        cur_group = 0
        group_of_nums = {}
        group_of_nums[min(nums)] = 0
        list_of_group = {}
        list_of_group[0] = deque([min(nums)])
        n = len(nums)
        for i in range(1, n):
            if nums_sorted[i] - nums_sorted[i - 1] > limit:
                cur_group += 1
            group_of_nums[nums_sorted[i]] = cur_group
            if cur_group not in  list_of_group:
                list_of_group[cur_group] = deque()
            list_of_group[cur_group].append(nums_sorted[i])
        for i in range(n):
            num = nums[i]
            group = group_of_nums[num]
            nums[i] = list_of_group[group].popleft()
        return nums
# Time O( n log n) Space O(n)