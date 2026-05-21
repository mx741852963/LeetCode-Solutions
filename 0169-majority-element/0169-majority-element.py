from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # return count.most_common(1)[0][0]
        # maxx = max(count.values())
        # inverted_dict = {v: k for k, v in count.items()}
        # target_key = inverted_dict.get(maxx)  
        # return target_key
        # Time O(n)
        # Space o(n)
        ans = -1
        count = 0
        for num in nums :
            if count == 0:
                ans = num
            if ans ==num:
                count +=1
            else :
                count -=1
        return ans
# Time O(n)
# Space O(1)