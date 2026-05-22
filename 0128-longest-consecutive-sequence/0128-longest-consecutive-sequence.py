# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_ = set(nums)
#         maxx = 0
#         for i in nums_:
#             if i - 1 not in nums_:
#                 next_num = i + 1
#                 count = 1
#                 while next_num in nums_:
#                     count += 1
#                     next_num += 1
#                 maxx = max(maxx, count)
#         return maxx
# # Time O(n)
# # Space O(n)
class Solution:
    def __init__(self):
        self.longest_sequence = 0
        self.num_to_preceding_sequence_length = dict()

    def longestConsecutive(self, nums: List[int]) -> int:
        # create a num_to_preceding_chain dict, do one pass and populate with every number in nums have a value of -1
        # do a second-pass - for each element in the dict where the value is -1, try to figure out the value. 
        # value(num) = does preceding elt exist ? value(preceding elt) : 1;
        # if the preceding element exists, keep tracing that back until the preceding element doesn't exist anymore, all the while populating the values. keep a variable that keeps track of the highest value
        
        for num in nums:
            self.num_to_preceding_sequence_length[num] = -1
        for num, preceding_sequence_length in self.num_to_preceding_sequence_length.items():
            self.getLengthOfChainEndingWithNum(num)

        return self.longest_sequence
        
    def getLengthOfChainEndingWithNum(self, num) -> int:
        if (self.num_to_preceding_sequence_length[num] != -1):
            return self.num_to_preceding_sequence_length[num]
        if (num - 1 not in self.num_to_preceding_sequence_length):
            self.num_to_preceding_sequence_length[num] = 1
        else:
            self.num_to_preceding_sequence_length[num] = self.getLengthOfChainEndingWithNum(num - 1) + 1
        if self.num_to_preceding_sequence_length[num] > self.longest_sequence:
            self.longest_sequence = self.num_to_preceding_sequence_length[num]        
        return self.num_to_preceding_sequence_length[num]