class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int: 
        n = 1 << max(nums). bit_length()
        x2 = set([0])
        x3 = set (nums)
        while nums:
            num = nums.pop()
            x3 |= {num ^ x2 for x2 in x2}         
            x2 |= {num ^ x1 for x1 in nums}  
            if len(x3) == n: break
 
        return len(x3)
# Time O(n^2 + n*2048)
# Space O(n + 2048)
        

        # n = 1 << max(nums).bit_length()
        # one, two, three = [0] * n, [0] * n, [0] * n
        # for num in nums:
        #     one[num] = 1
        #     for bit in range(n):
        #         if one[bit]:
        #             two[bit ^ num] = 1
        # for num in nums:
        #     for bit in range(n):
        #         if two[bit]:
        #             three[bit ^ num] = 1

        # return sum(three)
