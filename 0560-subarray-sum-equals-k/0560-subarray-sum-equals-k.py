class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        for prefix in accumulate(nums):
            if prefix - k in prefix_counts:
                count += prefix_counts[prefix - k]
            prefix_counts[prefix] += 1

        return count


# Time: O(N)
# Space: O(N)
