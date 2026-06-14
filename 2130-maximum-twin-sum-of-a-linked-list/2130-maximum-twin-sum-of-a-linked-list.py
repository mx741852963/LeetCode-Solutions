# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mapp = []
        while head:
            mapp.append(head.val)
            head = head.next
            
        n = len(mapp)
        summ = 0
        j = n - 1 
        for i in range(n//2):
            summ = max(summ,mapp[i] + mapp[j])
            j -=1
        return summ
