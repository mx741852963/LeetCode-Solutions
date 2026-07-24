class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = 1 << max(nums).bit_length()
        one, two, three = [0] * n, [0] * n, [0] * n
        for num in nums:
            one[num] = 1
            for bit in range(n):
                if one[bit]:
                    two[bit ^ num] = 1
        for num in nums:
            for bit in range(n):
                if two[bit]:
                    three[bit ^ num] = 1

        return sum(three)
