class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lenn = len(nums)
        l,r,piv = [],[],[]
        for i in range(lenn):
            if nums[i] > pivot:
                r.append(nums[i])
            elif nums[i] < pivot:
                l.append(nums[i])
            else:
                piv.append(nums[i])
        return  l + piv + r