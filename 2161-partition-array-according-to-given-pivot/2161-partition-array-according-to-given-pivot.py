class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,r,piv = [],[],[]
        for num in nums:
            if num > pivot:
                r.append(num)
            elif num < pivot:
                l.append(num)
            else:
                piv.append(num)
        l.extend(piv)
        l.extend(r)
        return  l 
# Time O(n)
# Space O(n)