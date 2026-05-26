# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        cur = head 
        while cur :
            d = id(cur)
            if  d not in sett:
                sett.add(d)
                cur = cur.next
            else :
                return True
        return False