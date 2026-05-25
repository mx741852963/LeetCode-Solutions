class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         lenn = len(nums)
#         l = 0
#         r = lenn - 1
#         while l < r:
#             min_index = (l + r) // 2
#             if nums[min_index] > nums[r]:
#                 l = min_index + 1
#             else:
#                 r = min_index
#         minn = l
#         if minn == 0:
#             l, r = 0, lenn - 1
#         elif nums[0] <= target <= nums[minn - 1]:
#             l, r = 0, minn - 1
#         else:
#             l, r = minn, lenn - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return -1 
# # Time = O(log n )
# # Space = O(1)