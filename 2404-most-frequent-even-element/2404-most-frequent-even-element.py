class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter,ans,max_freq = Counter(nums),-1,0
        for key, value in counter.items():
            if (key & 1) == 0:
                if value > max_freq or (value == max_freq and key < ans): max_freq,ans = value,key         
        return ans
# Time O(n)
# Space O(u)